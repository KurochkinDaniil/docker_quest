import os
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services import validate_answer, decrypt, load_key

app = FastAPI()
templates = Jinja2Templates(directory='')


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    if not os.environ.get("SECRET_KEY"):
        return templates.TemplateResponse("step1.html", {"request": request})
    else:
        if not validate_answer(os.environ.get("SECRET_KEY")):
            return "Ответ неверный, можете посмотреть ответ на вопрос и подсказку на предыдущем шаге"
        elif not os.path.exists('./app/files/chekhov.txt'):
            return templates.TemplateResponse("step2.html", {"request": request})
        else:
            return templates.TemplateResponse("step3.html", {'request': request})


@app.get("/files/{filename}")
def read_file(filename: str, q: Optional[str] = None, key=None):
    text = decrypt(f'app/files/{filename}', load_key())
    return {"Ответ": text}
