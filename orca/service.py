from typing import List
from kubernetes import client, config
from orca.models import QuestDB

class QuestDBService:
    def __init__ (self):
        config.load_incluster_config()
        self.k8sclient  = client.AppsV1Api()

    def create(self, questDB: QuestDB):
        self.k8sclient.

    def get(self, org: str, name: str) -> List[QuestDB]:
        pass

    def delete(self, org: str, name: str):
        pass