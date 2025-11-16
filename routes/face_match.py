from fastapi import APIRouter, UploadFile, File
from app.utils.face_engine import compare_faces

router = APIRouter()

@router.post("/match-face")
async def match_face(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = compare_faces(image_bytes)
    return {"status": "success", "result": result}
