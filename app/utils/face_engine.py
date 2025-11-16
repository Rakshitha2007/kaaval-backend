from deepface import DeepFace
import numpy as np
from PIL import Image
import io

def compare_faces(image_bytes):
    try:
        # Load uploaded image
        img = Image.open(io.BytesIO(image_bytes))

        # Convert to numpy array
        img_np = np.array(img)

        # DeepFace representation (embedding)
        embedding = DeepFace.represent(img_np, model_name="Facenet")[0]["embedding"]

        # TEMP RESULT: No database yet, return embedding only
        return {
            "match": False,
            "confidence": 0,
            "embedding_length": len(embedding),
            "message": "Face recognized. Database match coming next."
        }

    except Exception as e:
        return {"error": str(e)}
