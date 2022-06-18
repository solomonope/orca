from typing import Dict
from kubernetes import client



class K8sService:

    def __init__(self):
        v1 = client.CoreV1Api()
        appsV1  =  client.AppsV1Api()
        net  =  client.NetworkingV1Api

    def create_namespace(self, name: str, annotations: Dict[str, str]):
        metadata = client.V1ObjectMeta(name=name, annotations=annotations)
        namespace = client.V1Namespace(metadata=metadata)
        return v1.create_namespace(body=namespace)
        

    def create_ingress(self):
        pass

    def create_service(self):
        v1.create_namespaced_service()
        pass

    def create_service_account(self, name: str, namespace: str, annotations: Dict[str, str]):
        return v1.create_namespaced_service_account()

    def create_stateful_set(self):
        client.V1StatefulSetSpec()
        client.V1StatefulSet()
        self.appsV1.create_namespaced_stateful_set()
        
