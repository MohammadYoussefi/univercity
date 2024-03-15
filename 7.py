from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    Adress: str


@app.post("/")
async def create_item(information: Item):
    i = 0
    count = 0
    while i < len(information.Adress):
        if 48 <= ord(information.Adress[i]) <= 57:
            count += 1
            if count == len(information.Adress):
                return "آدرس وارد شده صحیح نیست"
        i += 1
    if count != len(information.Adress):
        if len(information.Adress) <= 100:
            return "آدرس وارد شده صحیح است"
        else:
            return "آدرس وارد شده صحیح نیست"