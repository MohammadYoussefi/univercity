from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    PhoneNumber: str


@app.post("/")
async def create_item(Phone: Item):
    count_num = 0
    if len(Phone.PhoneNumber) == 11:
        if str(Phone.PhoneNumber[0]) == "0":
            if str(Phone.PhoneNumber[1]) == "9":
                i = 2
                while i < 11:
                    if 48 <= ord(Phone.PhoneNumber[i]) <= 57:
                        count_num += 1
                    i += 1
            else:
                return  "شماره موبایل صحیح نیست"
        else:
            return "شماره موبایل صحیح نیست"
    else:
        return "شماره موبایل صحیح نیست"

    if len(Phone.PhoneNumber) == 11:
        if count_num == 9:
            return "شماره موبایل صحیح است"
        else:
            return "شماره موبایل صحیح نیست"