from fastapi import FastAPI
from routes.face_match import router as face_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kaaval Backend Running"}

app.include_router(face_router)
