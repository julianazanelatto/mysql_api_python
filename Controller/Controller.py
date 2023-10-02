from fastapi import APIRouter
from Controller.Routes import router as document_router

class CollectionController:
    def __init__(self):
        self.router = APIRouter()
        self.router.include_router(document_router)