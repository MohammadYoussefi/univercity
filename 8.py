from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    PostCode: int


@app.post("/")
async def create_item(Post: Item):
    count_digit = 0
    while Post.PostCode > 0:
        L = Post.PostCode // 10
        count_digit += 1
        Post.PostCode //= 10
    if count_digit == 10:
        return "کد پستی صحیح است"
    else:
       return "کد پستی صحیح نیست "
