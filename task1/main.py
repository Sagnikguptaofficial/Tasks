from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel

from TreeBst import Node, TreeBst
import pickle
from textblob import TextBlob
from pathlib import Path

class Item(BaseModel):
    val: int
    text: str


app = FastAPI()


@app.post("/sendval/")
async def sendval(item: Item):

    blob = TextBlob(item.text)
    lst = [i.capitalize() for i in blob.noun_phrases]

    # if Path("tree.pkl").is_file():
    #     with open('tree.pkl', 'rb') as f:
    #         tree = pickle.load(f)
    # else:
    #     tree = TreeBst(Node(0, ['root']))

    try:
        with open('tree.pkl', 'rb') as f:
            tree = pickle.load(f)
    except FileNotFoundError:
        tree = TreeBst(Node(0, ['root']))

    tree.insert(Node(item.val, lst))

    with open("tree.pkl", 'wb') as f:
        pickle.dump(tree, f)

    return item

@app.get("/")
async def getval():
    return {"message": "Hello Sagnik"}


# @app.get('/')
# async def root():
#     return {"message": "Hello World"}
