from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()


def main(user_id: str):
    return user_id


class User(BaseModel):
    id: int
    name: str
    joined: date


first_user = User(id=1, name="aseke", joined="2020-02-02")

second_user_data = {
    "id": 2,
    "name": "main",
    "joined": "2020-02-02"
}

second_user = User(**second_user_data)


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}
