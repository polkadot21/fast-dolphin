from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from constants import CorsConstants

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./")

app.add_middleware(CORSMiddleware,
                   allow_origins=CorsConstants.DEV_ORIGINS,
                   allow_headers=CorsConstants.DEV_HEADERS,
                   allow_methods=CorsConstants.METHODS,
                   allow_credentials=True,
                   )


@app.get("/", response_class=HTMLResponse)
async def render_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/privacy", response_class=HTMLResponse)
async def render_tos(request: Request):
    return templates.TemplateResponse("privacy.html", {"request": request})


@app.get("/rules", response_class=HTMLResponse)
async def render_rules(request: Request):
    return templates.TemplateResponse("rules_2.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/account", response_class=HTMLResponse)
async def render_account(request: Request):
    return templates.TemplateResponse("account.html", {"request": request})


@app.get("/workout", response_class=HTMLResponse)
async def render_workout_planner(request: Request):
    return templates.TemplateResponse("workout.html", {"request": request})


@app.get("/about-us", response_class=HTMLResponse)
async def render_about_us(request: Request):
    return templates.TemplateResponse("aboutus.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def render_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/signup", response_class=HTMLResponse)
async def render_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})