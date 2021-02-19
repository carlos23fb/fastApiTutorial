from fastapi import FastAPI
# TODO Importar fastApi

# TODO Crear una instancia
app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Hello World!!"}