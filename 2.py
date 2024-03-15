from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


@app.post("/")
def get_name(name: Item):
    i = 0
    P_count = 0
    while i < len(name.name):
        if len(name.name) <= 10:
            if 1568 <= ord(name.name[i]) <= 1610 or name.name[i] == "ی" or name.name[i] == "چ" or name.name[i] == "پ" or \
                    name.name[i] == "ک" or name.name[i] == "گ" or name.name[i] == "ژ":
                P_count += 1
            else:
                return "لطفا از حروف فارسی استفاده کنید!"
        else:
            return "طول اسم بیشتر از 10 کاراکتر است"
        i += 1

    if P_count == len(name.name):
        return "اسم صحیح است"
