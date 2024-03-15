from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    date: str


app = FastAPI()


@app.post("/")
async def create_item(num: Item):
    date_copy = num.date.split("/")
    if 1 <= int(date_copy[0]) <= 1402:
        if 1 <= int(date_copy[1]) <= 12:
            if 1 <= int(date_copy[2]) <= 31:
                return "تاریخ تولد صحیح است"
            else:
                return "روز تاریخ تولد اشتباه است!"
        else:
            return "ماه تاریخ تولد اشتباه است!"
    else:
        return "سال تاریخ تولد اشتباه است!"
