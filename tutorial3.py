import numpy as np
import cv2

# Open the video file
cap = cv2.VideoCapture('assets/bai.mp4')

while True:
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        break

    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame

    # Create a blank image of the same shape as the frame
    image = np.zeros(frame.shape, np.uint8)

    # Resize the frame to half its size
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Place the resized and rotated frames into the appropriate quadrants
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    # Display the image
    cv2.imshow('frame', image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
