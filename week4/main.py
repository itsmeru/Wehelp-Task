from fastapi import FastAPI,Request,Form,Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
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
        error_message="Please enter username and password"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    elif verify(request,username,password):
            return RedirectResponse(url="/member", status_code=303)
    else:
        error_message="Username or password is not correct"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
@app.route("/member",methods=["GET", "POST"])
async def member(request: Request):
    if request.method == "POST":
        return templates.TemplateResponse("./static/member.html", {"request": request})
    else:
        if "username" not in request.session:
            return RedirectResponse(url="/")
        else:
            return templates.TemplateResponse("./static/member.html", {"request": request})

@app.get("/error")
async def error(request: Request ,message: str):
    return templates.TemplateResponse("./static/error.html", {"request": request, "message": message})

@app.get("/singout")
async def singout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")


@app.post("/calculate")
async def calculate(num:int=Form(None)):
    return RedirectResponse(url=f"/square/{num}",status_code=303)
    

@app.get("/square/{num}")
async def square(request: Request,num:int):
    result = num ** 2
    return templates.TemplateResponse("./static/square.html", {"request": request, "num": result})


