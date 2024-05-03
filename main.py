import json

from fastapi import FastAPI

from models import Snowboard, Brand


app = FastAPI()


with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

snowboards: list[Snowboard] = []

for snowboard in snowboard_list:
    snowboards.append(Snowboard(**snowboard))


@app.get("/snowboards")
async def get_snowboards() -> list[Snowboard]:
    return snowboards

@app.post("/snowboards")
async def create_snowboards(snowboard: Snowboard) -> None:
    snowboards.append(snowboard)

@app.put("/snowboards/{id}")
async def update_snowboards(id: int, updated_snowboard: Snowboard) -> None:
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == id:
            snowboards[i] = updated_snowboard
            return
    snowboards.append(updated_snowboard)
    return
    
@app.delete("/snowboards/{id}")
async def delete_snowboards(id: int) -> None:
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == id:
            snowboards.pop(i)
            return