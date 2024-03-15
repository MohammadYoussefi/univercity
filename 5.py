from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    State: str


@app.post("/")
async def create_repo(State: Item):
    state = [
        "تهران",
        "بوشهر",
        "خوزستان",
        "اصفهان",
        "خراسان رضوی",
        "فارس",
        "آذربایجان شرقی",
        "مازندران",
        "کرمان",
        "البرز",
        "گیلان",
        "کهگیلویه و بویراحمد",
        "آذربایجان غربی",
        "هرمزگان",
        "اراک",
        "یزد",
        "	فرامنطقه ای",
        "کرمانشاه",
        "قزوین",
        "سیستان و بلوچستان",
        "همدان",
        "ایلام",
        "گلستان",
        "لرستان",
        "زنجان",
        "اردبیل",
        "قم",
        "کردستان",
        "سمنان",
        "چهارمحال و بختیاری",
        "خراسان شمالی",
        "خراسان جنوبی",
    ]
    if state[0] == State.State or state[1] == State.State or state[2] == State.State or state[3] == State.State \
            or state[4] == State.State or state[5] == State.State or state[6] == State.State \
            or state[7] == State.State or state[8] == State.State or state[9] == State.State \
            or state[10] == State.State or state[11] == State.State or state[12] == State.State \
            or state[13] == State.State or state[14] == State.State or state[15] == State.State \
            or state[16] == State.State or state[17] == State.State or state[18] == State.State \
            or state[19] == State.State or state[20] == State.State or state[21] == State.State \
            or state[22] == State.State or state[23] == State.State or state[24] == State.State \
            or state[25] == State.State or state[26] == State.State or state[27] == State.State \
            or state[28] == State.State or state[29] == State.State or state[30] == State.State \
            or state[31] == State.State:
        return "صحیح است"
    else:
        return "استان وارد شده نادرست است"
