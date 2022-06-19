from typing import Dict
from kubernetes import client

class K8sService:
    def __init__(self):
        self.coreV1Api = client.CoreV1Api()
        self.appsV1  =  client.AppsV1Api()

    def create_namespace(self, name: str, annotations: Dict[str, str]):
        metadata = client.V1ObjectMeta(name=name, annotations=annotations)
        namespace = client.V1Namespace(metadata=metadata)
        self.coreV1Api.g
        return self.coreV1Api.create_namespace(body=namespace)
        

    def create_ingress(self):
        pass

    def create_service(self):
        pass

    def create_service_account(self, name: str, namespace: str, annotations: Dict[str, str]):
        return self.coreV1Ap.create_namespaced_service_account()

    def create_stateful_set(self):
        client.V1StatefulSetSpec()
        client.V1StatefulSet()
        self.coreV1Api.create_namespaced_stateful_set()
        
