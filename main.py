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


@app.get("/tos", response_class=HTMLResponse)
async def render_tos(request: Request):
    return templates.TemplateResponse("tos.html", {"request": request})


@app.get("/rules", response_class=HTMLResponse)
async def render_rules(request: Request):
    return templates.TemplateResponse("rules.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/account", response_class=HTMLResponse)
async def render_account(request: Request):
    return templates.TemplateResponse("account.html", {"request": request})


@app.get("/workout", response_class=HTMLResponse)
async def render_workout_planner(request: Request):
    return templates.TemplateResponse("workout.html", {"request": request})
