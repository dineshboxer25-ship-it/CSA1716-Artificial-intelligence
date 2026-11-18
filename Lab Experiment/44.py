# Image Segmentation using OpenCV

import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("image.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold segmentation
    ret, segmented = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Display original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    # Display segmented image
    plt.subplot(1, 2, 2)
    plt.imshow(segmented, cmap="gray")
    plt.title("Segmented Image")
    plt.axis("off")

    plt.show()
