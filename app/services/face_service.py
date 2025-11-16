import face_recognition

def compare_faces(image1_path, image2_path):
    try:
        img1 = face_recognition.load_image_file(image1_path)
        img2 = face_recognition.load_image_file(image2_path)

        encode1 = face_recognition.face_encodings(img1)[0]
        encode2 = face_recognition.face_encodings(img2)[0]

        result = face_recognition.compare_faces([encode1], encode2)

        if result[0]:
            return True
        else:
            return False

    except Exception as e:
        return str(e)
