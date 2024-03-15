from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(StudentNumber: int):
    count = 0
    StudentNumber_copy = StudentNumber
    while StudentNumber_copy > 0:
        L = StudentNumber_copy % 10
        count += 1
        StudentNumber_copy //= 10
    if count != 11:
        return "شماره دانشجویی باید 11 رقم باشد. تعداد ارقام شماره دانشجویی وارد شده نادرست است."
    elif count == 11:
        if 400 <= StudentNumber // 100000000 <= 402:
            if ((StudentNumber % 100000000) // 100) == 114150:
                if 1 <= StudentNumber % 100 <= 99:
                    return " شماره دانشجویی وارد شده درست است.", StudentNumber
                else:
                    return "قسمت اندیس نادرست است"
            else:
                return "قسمت ثابت نادرست است. "
        else:
            return "قسمت سال نادرست است."
