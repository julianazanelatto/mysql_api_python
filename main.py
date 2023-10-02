from fastapi import FastAPI
from Controller.Controller import CollectionController

app = FastAPI()
controller = CollectionController()
app.include_router(controller.router)


if __name__ == '__main__':

   import uvicorn
   uvicorn.run(app, host="127.0.0.1", port=8000)