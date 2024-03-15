from fastapi import FastAPI

app = FastAPI()


@app.get("/{StudentNumber}")
async def read_StudentNumber(StudentNumber: int):
    count_student_number = 0
    StudentNumber_copy = StudentNumber
    while StudentNumber_copy > 0:
        L = StudentNumber_copy % 10
        count_student_number += 1
        StudentNumber_copy //= 10
    if count_student_number != 11:
        return "شماره دانشجویی باید 11 رقم باشد. تعداد ارقام شماره دانشجویی وارد شده نادرست است."
    elif count_student_number == 11:
        if 400 <= StudentNumber // 100000000 <= 402:
            if ((StudentNumber % 100000000) // 100) == 114150:
                if 1 <= StudentNumber % 100 <= 99:
                    return " شماره دانشجویی وارد شده درست است.", StudentNumber
                else:
                    return "قسمت اندیس شماره دانشجویی نادرست است"
            else:
                return "قسمت ثابت شماره دانشجویی نادرست است. "
        else:
            return "قسمت سال شماره دانشجویی نادرست است."
