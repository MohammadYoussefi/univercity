from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    marital_status: str


@app.post("/")
async def marital_status(item: Item):
    if item.marital_status == "مجرد" or item.marital_status == "متاهل":
        if item.marital_status == "مجرد":
            return "صحیح است"
        else:
            return "صحیح است"
    else:
        return "جواب نادرست است"