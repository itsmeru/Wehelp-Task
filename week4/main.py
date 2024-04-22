from fastapi import FastAPI,Request,Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse,HTMLResponse
from starlette_session import SessionMiddleware
app=FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    SessionMiddleware,
    secret_key="some-random-string",
    max_age=None,
    cookie_name="user_session"
)
templates = Jinja2Templates(directory=".")
app.mount("/static", StaticFiles(directory="static"))

    
def verify(request: Request,username,password):
    if username=="test" and password=="test":
        request.session["username"] = username
        return True
    else:
        return False
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("./static/index.html", {"request": request})

@app.post("/signin")
async def signIn(request:Request,username:str=Form(None),password:str=Form(None)):
    if not username or not password:
        message="Please enter username and password"
        redirect_url = f"/error?message={message}"
        return RedirectResponse(url=redirect_url)
    elif verify(request,username,password):
            return RedirectResponse(url="/member")
    else:
        message="Username or password is not correct"
        redirect_url = f"/error?message={message}"
        return RedirectResponse(url=redirect_url)
    
@app.route("/member",methods=["GET", "POST"])
async def member(request: Request):
    if request.method == "POST":
        return templates.TemplateResponse("./static/member.html", {"request": request})
    else:
        if "username" not in request.session:
            return RedirectResponse(url="/")
        else:
            return templates.TemplateResponse("./static/member.html", {"request": request})

@app.post("/error")
async def error(request: Request, message):
    return templates.TemplateResponse("./static/error.html", {"request": request,"message":message})

@app.get("/singout")
async def singout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")

@app.post("/square")
async def square(request:Request, num:int=Form(...)):
    result=num**2
    return templates.TemplateResponse("./static/square.html",{"request":request,"num":result})



