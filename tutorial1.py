import cv2

img = cv2.imread('assets/bai.jpg', -1)

# Resize the image
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Rotate the image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save the modified image
cv2.imwrite('new_img.jpg', img)

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
