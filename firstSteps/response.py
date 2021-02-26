from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel, EmailStr

app = FastAPI()


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
}





class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None




@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


# @app.post("/user/", response_model= UserIn)
# async def create_user(user: UserIn):
#     return user


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user




@app.get("/item/read/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]