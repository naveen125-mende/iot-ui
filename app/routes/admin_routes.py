from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/",response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse("admin/admin-login.html",{ "request":request })

@router.get("/home",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("admin/admin-dashboard.html",{ "request":request })

@router.get("/profile",response_class=HTMLResponse)
async def profile(request:Request):
    return templates.TemplateResponse("admin/admin-profile.html",{ "request":request })