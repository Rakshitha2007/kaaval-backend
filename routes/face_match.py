from fastapi import APIRouter, UploadFile, File
from utils.face_engine import compare_faces

router = APIRouter(prefix="/face")

@router.post("/match")
async def face_match(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    image1 = await file1.read()
    image2 = await file2.read()

    result = compare_faces(image1, image2)

    return {
        "match": result["match"],
        "confidence": result["confidence"]
    }
