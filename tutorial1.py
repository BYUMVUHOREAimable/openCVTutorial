import cv2

# Read the image
img = cv2.imread('assets/bai.jpg', -1)
# 0 for grayscale, -1 for original color

# Resize the image to half the size
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Rotate the image 90 degrees clockwise
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)

# Display the image in a window
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
