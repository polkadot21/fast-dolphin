from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from constants import CorsConstants
from dotenv import load_dotenv
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CorsConstants.DEV_ORIGINS,
    allow_headers=CorsConstants.DEV_HEADERS,
    allow_methods=CorsConstants.METHODS,
    allow_credentials=True,
)


# Load the environment variables from the .env file
load_dotenv()

# Define a global variable for the environment variables
env = {
    'BACKEND_URL': os.getenv('BACKEND_URL'),
    'VERSION': os.getenv('VERSION'),
}

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
    return templates.TemplateResponse("login.html", {"request": request, "env": env})


@app.get("/logout", response_class=HTMLResponse)
async def render_account(request: Request):
    return templates.TemplateResponse("logout.html", {"request": request, "env": env})


@app.get("/account", response_class=HTMLResponse)
async def render_account(request: Request):
    return templates.TemplateResponse("account.html", {"request": request, "env": env})


@app.get("/training-plans", response_class=HTMLResponse)
async def render_account(request: Request):
    return templates.TemplateResponse("training-plans.html", {"request": request, "env": env})


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

@app.get("/new-customer-request", response_class=HTMLResponse)
async def render_customer_request(request: Request):
    return templates.TemplateResponse("customer-request.html", {"request": request, "env": env})

@app.get("/successfully-submitted", response_class=HTMLResponse)
async def render_successfully_submitted(request: Request):
    return templates.TemplateResponse("successfully-submitted.html", {"request": request})


@app.get("/password_reset", response_class=HTMLResponse)
async def render_reset_password(request: Request):
    return templates.TemplateResponse("reset-password.html", {"request": request})


@app.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(request: Request):
    return templates.TemplateResponse(
        "404.html", {"request": request}, status_code=status.HTTP_404_NOT_FOUND
    )
