import cv2
import random

# Load the image
img = cv2.imread('assets/bai.jpg', -1)

print(img)  # Print the pixel values
print(type(img))  # Print the type of the image array
print(img.shape)  # Print the shape of the image
print(img[257][400])  # Print the pixel value at (257, 400)

# Extract the region of interest from the original image
tag = img[500:700, 600:670]  # Adjusting this to match the width of 70

# Insert the tag into the main image
img[100:300, 650:720] = tag  # Ensure this matches 'tag' dimensions

# Modify the first 100 rows of the image
for i in range(100):
    for j in range(img.shape[1]):
        # Assign random colors to the pixel at (i, j)
        img[i][j] = [random.randint(0, 255) for _ in range(3)]  # Random RGB values

# Display the modified image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
