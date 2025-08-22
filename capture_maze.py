import cv2
def capture_img():
# Initialize the camera (0 is usually the default camera, change if needed)
    camera = cv2.VideoCapture(1)

    if not camera.isOpened():
        print("Error: Could not open camera.")
    else:
        print("Press 'c' to capture and save the image or 'q' to quit.")
        while True:
            # Capture frame-by-frame
            ret, frame = camera.read()
            if not ret:
                print("Failed to grab frame.")
                break

            # Display the frame
            cv2.imshow('Camera', frame)

            # Wait for user input
            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                # Save the captured image
                image_path = 'input_maze/maze1.png'
                cv2.imwrite(image_path, frame)
                print(f"Image saved as {image_path}")
            elif key == ord('q'):
                # Quit the program
                break

    # Release the camera and close all OpenCV windows
    camera.release()
    cv2.destroyAllWindows()