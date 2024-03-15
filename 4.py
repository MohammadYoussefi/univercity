from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    serial: str


@app.post("/")
def create_item(code: Item):
    count_num = 0
    count_letters = 0
    count_digits = 0

    if len(code.serial) == 9:
            for j in range(0, 6):
                if 48 <= ord(code.serial[j]) <= 57:
                    count_num += 1
                    if count_num == 6:
                        if 1570 <= ord(code.serial[6]) <= 1610 or code.serial[6] == "ی" or code.serial[6] == "ژ" or code.serial[6] == "ک" \
                                or code.serial[6] == "پ" or code.serial[6] == "گ" or code.serial[6] == "چ":
                            count_letters += 1
                            if count_letters != 1:
                                return "سریال شناسنامه صحیح نیست"
    if len(code.serial) == 9 and count_num == 6 and count_letters == 1:
        for k_serial in range(7, 9):
            if 48 <= ord(code.serial[k_serial]) <= 57:
                count_digits += 1

    if len(code.serial) == 9 and count_num == 6 and count_letters == 1 and count_digits == 2:
        return "سریال شناسنامه صحیح است"
    else:
        return " سریال شناسنامه صحیح نیست"

