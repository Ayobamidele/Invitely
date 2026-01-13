from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello from FastAPI !"})

app.include_router(user.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")