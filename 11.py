from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    College: str

@app.post("/")
async def root(college: Item):
    colleges = [
        "فنی و مهندسی",
        "علوم پایه",
        "علوم انسانی",
        "دامپزشکی",
        "اقتصاد",
        "کشاورزی",
        "منابع طبیعی"
    ]
    i = 0
    count_word = 0
    while i < 7:
        if college.College == colleges[i]:
            count_word += 1
        i += 1
    if count_word == 1:
        return  "دانشکده مجاز است"
    else:
        return "دانشکده اشتباه است"
