from fastapi import UploadFile
from app.services.face_service import compare_faces
import shutil
import uuid
import os

UPLOAD_DIR = "uploads"

# Create upload folder if not exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def process_face_match(file1: UploadFile, file2: UploadFile):
    # Generate random file names
    file1_name = f"{uuid.uuid4()}_{file1.filename}"
    file2_name = f"{uuid.uuid4()}_{file2.filename}"

    file1_path = os.path.join(UPLOAD_DIR, file1_name)
    file2_path = os.path.join(UPLOAD_DIR, file2_name)

    # Save files
    with open(file1_path, "wb") as f:
        shutil.copyfileobj(file1.file, f)

    with open(file2_path, "wb") as f:
        shutil.copyfileobj(file2.file, f)

    # Compare faces using service
    result = compare_faces(file1_path, file2_path)

    return {
        "match": result
    }
