from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
# TODO Importar fastApi

# TODO Crear una instancia
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {
	"item_name": "Bar"}, {"item_name": "Baz"}]


class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"


class Item(BaseModel):
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None


# @app.post("/items/")
# async def create_item(item: Item):
#     item.name + item.price
#     return item

@app.post("/items/")
async def create_item(item: Item):
	item_dict = item.dict()
	if item.tax:
		price_with_tax = item.price + item.tax
		item_dict.update({"price_with_tax": price_with_tax})
	return item_dict


@app.get("/")
async def root():
	return {"message": "Hello World!!"}


@app.get("/users/me")
async def read_user_me():
	return {"user_id": "usuario actual"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
	return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):

	if model_name == ModelName.alexnet.value:
		return {"model_name": model_name, "message": "Deep Learning FTW!"}

	if model_name.value == "lennet":
		return {"model_name": model_name, "message": "LeCNN all the images"}

	return {"model_name": model_name, "message": "Have some residuals"}

# TODO Path parameters containing paths


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
	return {"file_path": file_path}


# TODO Optional Parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# TODO Query parameter type conversion
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
	item = {"item_id": item_id}
	if q:
		item.update({"q": q})
	if not short:
		item.update({"short": "This is amazing item has a long description"})
	return item

# TODO Multiple path and query params

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item

# TODO Required query params

# @app.get("/item/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item= {"item_id": item_id, "needy": needy}
#     return item


# TODO Optional and default query params
@app.get("/item/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
	item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
	return item
