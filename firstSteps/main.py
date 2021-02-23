from typing import List, Optional, Set
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
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


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(None, title="The description of the item", max_length=300)
#     price: float = Field(
#         ..., description="The price must be greater than zero")
#     tax: Optional[float] = None

# TODO Add "Image" Model as nested field to Item Model

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None


# TODO Modify 'tag' Item model field from a List with string type parameters to a Set with strings type parameters

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = set()

# TODO List fields with string type parameter

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: List[str] = []


# TODO List Fields

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: list = []


class User(BaseModel):
    user_name: str
    full_name: Optional[str] = None

# TODO Embed a single body parameter

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(...)):
    results = {"item_id": item_id, "item": item}
    return results



# TODO Multiple body params and query

# @app.put("/items/{item_id}")
# async def update_items(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: int = Body(..., gt=0),
#     q: Optional[str] = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results


# TODO Singular values in body

# @app.put("/items/{item_id}")
# async def update_items(
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: int = Body(..., ge=1, le=5)
# ):
#     result = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return result


# TODO Multiple body parameters

# @app.put("/items/{item_id}")
# async def update_items(
#     item_id: int,
#     item: Item,
#     user: User
# ):
#     result ={"item_id": item_id, "item": item, "user": user}
#     return result


# TODO Mix Path, Query and body parameters

# @app.put("/items/{item_id}")
# async def update_items(
#     *,
#     item_id: int = Path(..., title="The Id of the item to get", ge=0, le=1000),
#     q: Optional[str] = None,
#     item: Optional[Item] = None
# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     if item:
#         result.update({"item": item})
#     return result





#TODO Number Validations: greater than equal, greater than, less than with floats

# @app.get("/items/{item_id}")
# async def read_item(
#     *,
#     item_id: int = Path(..., title="The item Id of the item to get", gt=0, le=10),
#     q: str,
#     size: float = Query(..., gt=0, lt=10.5)
# ):
#     result = {"item_id": item_id, "q": q, "size": size}
#     return result




# TODO Number Validations: greater than equal

# @app.get("/items/{item_id}")
# async def read_item(
#     *,
#     item_id: int = Path(..., title="The item Id of the item to get", gt=0, le=10),
#     q: str
# ):
#     results = {"item_id": item_id, "q": q}
#     return results 




# TODO Ordering the parameters as is needed and tricks 


# @app.get("/items/{item_id}")
# async def read_items(
#     *,
#     item_id: int = Path(..., title="The item Id of the item to get"),
#     q: str
# ):
#     result = {"item_id": item_id, "q": q}
#     return result


# TODO Ordering the parameters as is needed

# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: int = Path(..., title="The Id of the item to get")
# ):
#     results = {"item_id": item_id, "q": q}
#     return results


# TODO Import path

# @app.get('/items/{item_id}')
# async def read_items(
#     item_id: int = Path(..., title="The Id of the item to get"),
#     q: Optional[str] = Query(None, alias="item-query")
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# TODO Deprecating parameters

# @app.get("/items/")
# async def read_items(
#     q: Optional[str] = Query(
#         None,
#         alias="item-query",
#         title="Query String",
#         description="Query String for the items to search in the database that have a good match",
#         min_length=3,
#         max_length=20,
#         regex="^fixedquery$",
#         deprecated= True
#     )
# ):
#     results = {"items": [{"item_id": "Foor"},{"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# TODO Alias parameters


# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, alias="item-query")):
#     results = {"items": [{"item_id": "Foo"},{"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# TODO Add more metadata


# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None,
#                                         min_length=3, 
#                                         title="Query Strinig",
#                                         description="Query String for items to search in the database that have a good match")):
#     results = {"items": [{"id_item": "Foo"},{"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# TODO Query parameter only 

# @app.get("/items/")
# async def read_items(q: Optional[List[int]] = Query([])):
#     query_items = {"q": q}
#     return query_items



# TODO Query parameter list / multiple values

# @app.get("/items/")
# async def read_items(q: Optional[List[str]] = Query(None)):
#     query_items = {"q": q}
#     return query_items



# TODO Make query parameter required


# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"},{"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# TODO Default values for query parameter

# @app.get("/items/")
# async def read_items(q: Optional[str] = Query("fixedquery", min_length=3)):
#     results = {"items": [{"item_id": "Foo"},{"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# TODO Add Regular
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, min_length = 3, max_length = 20, regex="^fixedquery$")):
#     results = {"item": [{"item_id": "Foo"},{"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# TODO Add more validations


# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# TODO Aditional Validation

# @app.get("/items/")
# async def read_item(q: Optional[str] = Query(None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# TODO Query parameters and String Validations


# @app.get("/items/")
# async def read_items(q: str = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.post("/items/")
# async def create_item(item: Item):
#     item.name + item.price
#     return item

# TODO Request body + path + query params


@app.put("/items/create/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# TODO Request Body + path parameters

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
# 	return {"item_id": item_id, **item.dict()}


# TODO Using the model attributes

# @app.post("/items/")
# async def create_item(item: Item):
# 	item_dict = item.dict()
# 	if item.tax:
# 		price_with_tax = item.price + item.tax
# 		item_dict.update({"price_with_tax": price_with_tax})
# 	return item_dict


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
@app.get("/items/read/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# TODO Query parameter type conversion
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
# 	item = {"item_id": item_id}
# 	if q:
# 		item.update({"q": q})
# 	if not short:
# 		item.update({"short": "This is amazing item has a long description"})
# 	return item

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
