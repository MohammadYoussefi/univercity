from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    Landline_phone: int


@app.post("/")
async def create_item(Phone: Item):
    count_land_line = 0
    land_line_copy = str(Phone.Landline_phone)
    i_land_line = 0
    while i_land_line < len(land_line_copy):
        if 48 <= ord(land_line_copy[i_land_line]) <= 57:
            count_land_line += 1
        i_land_line += 1
    if count_land_line == 8:
        return "شماره تلفن ثابت صحیح است"
    else:
        return "شماره تلفن ثابت نادرست است"