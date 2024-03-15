from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    nation_code: int


@app.post("/")
async def nation_code(item: Item):
    nation_code_ccpy = str(item.nation_code)
    l_nation = len(nation_code_ccpy)
    sum_nation = 0
    for i_nation in range(0, l_nation - 1):
        c_nation = ord(nation_code_ccpy[i_nation])
        c_nation -= 48
        sum_nation = sum_nation + c_nation * (l_nation - i_nation)
        r_nation = sum_nation % 11
        c_nation = ord(nation_code_ccpy[l_nation - 1])
        c_nation -= 48
        if r_nation >= 2:
            r_nation = 11 - r_nation
    if r_nation == c_nation:
        return "کد ملی صحیح است"
    else:
        return "کد ملی صحیح نمی باشد"