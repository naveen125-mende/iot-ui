from fastapi import APIRouter, Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
from app.models.database_model import users
from app.db.database import database
from datetime import datetime,timezone
import random

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

generated_otp = None

@router.get("/", response_class=HTMLResponse)
async def show_login_form(request: Request):
    return templates.TemplateResponse("user/user-login.html", {"request": request})

@router.post("/")
async def handle_login_form(request: Request, username: str = Form(...), email: str = Form(...)):
    request.session['email'] = email 
    result = await database.fetch_one(users.select().where(users.c.username == username))
    date_time = datetime.now(timezone.utc)
    generated_otp = str(random.randint(100000, 999999))
    if not result:
        insert_query = users.insert().values(
            username=username,
            email=email,
            otp=generated_otp,
            generated_at=date_time
        )
        await database.execute(insert_query)
    return RedirectResponse(url="/user-otp", status_code=302)

@router.get("/user-otp")
async def get_otp_page(request: Request):
    email = request.session.get("email")
    if not email:
        return RedirectResponse(url="/", status_code=302)
    return templates.TemplateResponse("user/user-otp.html", {"request": request, "email": email})

@router.post("/user-otp")
async def verify_otp(request: Request, otp: str = Form(...)):
    email = request.session.get("email")
    if not email:
        return RedirectResponse(url="/", status_code=302)
    result = await database.fetch_one(users.select().where(users.c.email == email))
    if result and result.otp == otp:
        request.session.pop("email", None)
        return RedirectResponse(url="/user-dashboard", status_code=302)
    return templates.TemplateResponse("user/user-otp.html", {
        "request": request,
        "email": email,
        "error": "invalid"
    })

@router.get("/user-dashboard", response_class=HTMLResponse)
async def user_dashboard(request: Request):
    return templates.TemplateResponse("user/user-dashboard.html", {"request": request})