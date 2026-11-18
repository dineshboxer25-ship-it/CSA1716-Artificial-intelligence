# Face Recognition using DeepFace

from deepface import DeepFace

# Compare two face images
result = DeepFace.verify(
    img1_path="person1.jpg",
    img2_path="person2.jpg",
    model_name="Facenet"
)

print("Face Recognition Results")

print("Same Person:", result["verified"])

print("Distance:", result["distance"])

print("Threshold:", result["threshold"])

if result["verified"]:
    print("Both images belong to the same person.")
else:
    print("The images belong to different people.")
