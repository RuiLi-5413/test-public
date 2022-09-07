import ray
import requests
from fastapi import FastAPI
from ray import serve
import logging

app = FastAPI()
logger = logging.getLogger("ray.serve")

@serve.deployment(route_prefix="/hello")
@serve.ingress(app)
class MyFastAPIDeployment:
    def __init__(self):
        # import easyocr
        logger.info("All loaded")

    @app.get("/")
    def root(self):
        return "Hello1"

dag_graph = MyFastAPIDeployment.bind()