from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    StudentNumber: int


@app.post("/")
async def Student_Number(item: Item):
    count_student_number = 0
    StudentNumber_copy = item.StudentNumber
    while StudentNumber_copy > 0:
        L = StudentNumber_copy % 10
        count_student_number += 1
        StudentNumber_copy //= 10
    if count_student_number != 11:
        return "شماره دانشجویی باید 11 رقم باشد. تعداد ارقام شماره دانشجویی وارد شده نادرست است."
    elif count_student_number == 11:
        if 400 <= item.StudentNumber // 100000000 <= 402:
            if ((item.StudentNumber % 100000000) // 100) == 114150:
                if 1 <= item.StudentNumber % 100 <= 99:
                    return " شماره دانشجویی وارد شده درست است.", item.StudentNumber
                else:
                    return "قسمت اندیس شماره دانشجویی نادرست است"
            else:
                return "قسمت ثابت شماره دانشجویی نادرست است. "
        else:
            return "قسمت سال شماره دانشجویی نادرست است."
