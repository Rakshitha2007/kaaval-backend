from fastapi import APIRouter, UploadFile, File
from app.controllers.face_controller import process_face_match

router = APIRouter()

@router.post("/match-faces")
async def match_faces(image1: UploadFile = File(...), image2: UploadFile = File(...)):
    """
    Upload two images and get whether the faces match.
    """
    result = await process_face_match(image1, image2)
    return result
