import mysql.connector
from passlib.context import CryptContext
from fastapi import FastAPI,Request,Form,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from starlette_session import SessionMiddleware
from starlette.responses import JSONResponse
# from typing import Optional
def connect_mysql(db_name):
    con=mysql.connector.connect(
        user="root",
        password="betty520",
        host="localhost",
        database=db_name
    )
    return con
    
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    SessionMiddleware,
    secret_key="some-random-string",
    max_age=None,
    cookie_name="session_data",
)

templates = Jinja2Templates(directory=".")
app.mount("/static", StaticFiles(directory="static"))
def verify(request: Request,username,password):
    con=connect_mysql("website")
    cursor=con.cursor()

    cursor.execute("SELECT * FROM member WHERE username=%s", (username,))
    existing_user = cursor.fetchone() 
    if existing_user:
        hash_pwd=existing_user[3]
        if verify_password(password,hash_pwd):
            request.session["user_session"] = existing_user[2]
            request.session["page_name"] = existing_user[1]
            request.session["user_id"] = existing_user[0]
            con.close()
            return True
        else:
            con.close()
            return False
    else:
        con.close()
        return False
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("./static/mysql.html", {"request": request})

@app.post("/signup")
async def register(request:Request,name:str=Form(None),username:str=Form(None),password:str=Form(None)):
    con=connect_mysql("website")
    cursor=con.cursor()    
    cursor.execute("SELECT * FROM member WHERE username=%s", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        error_message="Repeated username in the page."
        return RedirectResponse(url=f"/error?message={error_message}",status_code=303)
        # raise HTTPException(status_code=422, detail="Username already exists")
    
    cursor.execute("INSERT INTO member(name,username,password) VALUES(%s,%s,%s)",(name,username,hash_password(password)))
    con.commit()
    con.close()
    return RedirectResponse(url="/",status_code=303)

@app.post("/signin")
async def signIn(request:Request,username:str=Form(None),password:str=Form(None)):
    if verify(request,username,password):
            return RedirectResponse(url=f"/member", status_code=303)
    else:
        error_message="Username or password is not correct"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
@app.get("/member")
async def member(request: Request):
    if "user_session" not in request.session:
        return RedirectResponse(url="/")
    else:
        memberId=request.session.get("user_id")
        pageName = request.session.get("page_name")
        con = connect_mysql("website")
        cursor = con.cursor()
        cursor.execute("SELECT message.id,message.member_id,member.name, message.content FROM message JOIN member ON message.member_id=member.id")
        messages = cursor.fetchall()
        return templates.TemplateResponse("./static/member.html", {"request": request,"pageName":pageName,"messages":messages,"memberId":memberId})

@app.get("/error")
async def error(request: Request ,message: str):
    return templates.TemplateResponse("./static/error.html", {"request": request, "message": message})

@app.get("/singout")
async def singout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")

@app.post("/createMessage")
async def createMessage(request:Request,content:str=Form(None)):
    con=connect_mysql("website")
    cursor=con.cursor()
    user_id= request.session.get("user_id")
    cursor.execute("INSERT INTO message(member_id,content) VALUES(%s,%s)",(user_id,content))
    con.commit()
    con.close()
    return RedirectResponse(url="/member",status_code=303)

@app.delete("/deleteMessage/{messageId}")
async def delete_message(request:Request,messageId: int):
    current_user_id = request.session.get("user_id")
    con=connect_mysql("website")
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT member_id FROM message WHERE id = %s", (messageId,))
            result = cursor.fetchone()
            if result is None:
                raise HTTPException(status_code=404, detail="Message not found")
            if result[0] != current_user_id:
                raise HTTPException(status_code=403, detail="You do not have permission to delete this message")

            cursor.execute("DELETE FROM message WHERE id = %s", (messageId,))
            con.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
    finally:
        con.close()

    return {"message": "OK"}
    
    


