from typing import List
from fastapi import FastAPI
from orca.models import QuestDB
from orca.service import QuestDBService

app = FastAPI()
questDBService = QuestDBService()

@app.get("/health")
def health():
    return {"ping": "pong"}


@app.post("/v1/questdb")
def create_quest_database(questDB: QuestDB) -> QuestDB:
    return questDBService.create(questDB)


@app.get("/v1/questdb")
def get_quest_database(org: str, name: str) -> List[QuestDB]:
    return questDBService.get(org, name)


@app.delete("/v1/questdb")
def delete_quest_database(transaction: any):
    return []
