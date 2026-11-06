
# from pathlib import Path
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates  ## For HTML & CSS Contents..!!..,,;;
# from app.api.routes import router
# from app.core.config import get_settings, BASE_DIR
# from app.core.logging import configure_logging
# from app.services.audit import init_db


# configure_logging()
# settings = get_settings()
# init_db()

# ## app object:-:-:_:_.,;;.,;;
# app = FastAPI(title=settings.app_name, version="1.0.0") ##--

# app.include_router(router)
# ## router to access the HTML and the CSS files.,;;..!!..,,;;..!!..,,;;    
# app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
# templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# ## default route :-:-:_:_
# @app.get("/", response_class=HTMLResponse)
# def home(request: Request):
#     ## som/ so whenever the user will execute my app; they will see the index.html page..!!..,,;;    ..!!..,,;;    
#     return templates.TemplateResponse("index.html", {"request": request, "app_name": settings.app_name})

from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.routes import router
from app.core.config import get_settings, BASE_DIR
from app.core.logging import configure_logging
from app.services.audit import init_db


configure_logging()
settings = get_settings()
init_db()


app = FastAPI(title=settings.app_name, version="1.0.0")

app.include_router(router)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    #return templates.TemplateResponse("index.html", {"request": request, "app_name": settings.app_name})
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "app_name": settings.app_name
    }
)
