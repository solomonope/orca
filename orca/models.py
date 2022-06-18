from pydantic import BaseModel

class QuestDB(BaseModel):
    organisation_name: str
    database_name: str