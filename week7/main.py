import mysql.connector
from passlib.context import CryptContext
from fastapi import FastAPI,Request,Form,HTTPException,Cookie
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from starlette_session import SessionMiddleware
from math import ceil
import secrets

app=FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None, openapi_url = None)
def generate_csrf_token():
    return secrets.token_hex(32)
@app.middleware("http")
async def add_csrf_token_to_session(request: Request, call_next):
    csrf_token = generate_csrf_token()
    request.session["csrf_token"] = csrf_token
    response = await call_next(request)
    return response
def connect_mysql(db_name):
    con=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database=db_name
    )
    return con
    
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

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
    cookie_name="csrf_token",
    # cookie_secure=True,
    # cookie_httponly=True  
)

class updatename(BaseModel):
    name:str
templates = Jinja2Templates(directory=".")
app.mount("/static", StaticFiles(directory="static"))
def verify(request: Request,username,password):
    con=connect_mysql("website")
    with con.cursor() as cursor:
        cursor.execute("SELECT * FROM member WHERE username=%s", (username,))
        existing_user = cursor.fetchone() 
        if existing_user:
            hash_pwd=existing_user[3]
            if verify_password(password,hash_pwd):
                request.session["user_session"] = existing_user[2]
                request.session["page_name"] = existing_user[1]
                request.session["user_id"] = existing_user[0]
                return True
            else:
                return False
        else:
            return False
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("./static/mysql.html", {"request": request})

@app.post("/signup")
async def register(request:Request,name:str=Form(None),username:str=Form(None),password:str=Form(None)):
    con=connect_mysql("website")
    with con.cursor() as cursor:
        cursor.execute("SELECT * FROM member WHERE username=%s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            error_message="Repeated username in the page."
            return RedirectResponse(url=f"/error?message={error_message}",status_code=303)
            # raise HTTPException(status_code=422, detail="Username already exists")
        
        cursor.execute("INSERT INTO member(name,username,password) VALUES(%s,%s,%s)",(name,username,hash_password(password)))
        con.commit()
    return RedirectResponse(url="/",status_code=303)

@app.post("/signin")
async def signIn(request:Request,username:str=Form(None),password:str=Form(None)):
    # csrf_token_from_request = request.cookies.get("csrf_token")
    # csrf_token_from_session = request.session.get("csrf_token")
    # if csrf_token_from_request != csrf_token_from_session:
    #     # print("請求：",csrf_token_from_request)
    #     # print("繪畫：",csrf_token_from_session)
    #     raise HTTPException(status_code=403, detail="CSRF token does not match")
    if verify(request,username,password):
            return RedirectResponse(url=f"/member", status_code=303)
    else:
        error_message="Username or password is not correct"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
@app.get("/member")
async def member(request: Request, page: int = 1, per_page: int = 10):
    if "user_session" not in request.session:
        return RedirectResponse(url="/")
    else:
        memberId=request.session.get("user_id")
        pageName = request.session.get("page_name")
        con = connect_mysql("website")
        with con.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM message")
            total_msg = cursor.fetchone()[0]
            total_pages = ceil(total_msg/per_page)
            offset = (page-1)*per_page
            cursor.execute("SELECT message.id,message.member_id,member.name, message.content FROM message JOIN member ON message.member_id=member.id ORDER BY message.time DESC LIMIT %s OFFSET %s",(per_page,offset))
            messages = cursor.fetchall()
            return templates.TemplateResponse("./static/member.html", {"request": request,"pageName":pageName,"messages":messages,"memberId":memberId,"total_pages": total_pages, "current_page": page})

@app.get("/api/member")
async def memberApi(request:Request,username:str=None):
    if username == None or "user_session" not in request.session:
        return {"data":"null"}
    else:
        con = connect_mysql("website")
        with con.cursor() as cursor:
            cursor.execute("SELECT id,name,username FROM member WHERE username=%s",(username,))
            result=cursor.fetchone()
            if result:
                return {
                    "data":{
                        "id":result[0],
                        "name":result[1],
                        "username":result[2]
                    } 
                }
            else:
                return {"data":"查無此人"}

@app.patch("/api/member")
async def updateName(request:Request,name:updatename):
    member_name = request.session.get("page_name")

    con = connect_mysql("website")
    with con.cursor() as cursor:
        cursor.execute("UPDATE member SET name=%s WHERE name=%s",(name.name,member_name))
        request.session["page_name"]=name.name
        con.commit()
        if cursor.rowcount>0:
            return{"ok":True}
        else:
            return{"error":True}
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
    with con.cursor() as cursor:
        user_id= request.session.get("user_id")
        cursor.execute("INSERT INTO message(member_id,content) VALUES(%s,%s)",(user_id,content))
        con.commit()
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
    
    


