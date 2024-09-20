from fastapi import FastAPI
from controller import list_de_controller

app = FastAPI()

app.include_router(list_de_controller.listde_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}



