from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    Subject: str


@app.post("/")
async def subject_list(item: Item):
    subjects = [
        "مهندسی برق-الکترونیک",
        " مهندسی شهرسازی",
        "مهندسی کامپیوتر",
        "مهندسی عمران",
        "مهندسی برق-قدرت",
        "مهندسی مکانیک و پلیمر",
        "مهندسی معدن"
    ]
    i = 0
    count_subject = 0
    while i < 7:
        if item.Subject == subjects[i]:
            count_subject += 1
        i += 1
    if count_subject == 1:
        return "رشته تحصیلی به درستی وارد شده است"
    else:
        return "رشته تحصیلی نادرست است"