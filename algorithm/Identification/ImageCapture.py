import cv2
import tkinter as tk
from tkinter import messagebox

def capture_images_with_notification():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return
    image_count = 0
    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    root = tk.Tk()
    root.withdraw()
    v_key_pressed = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame from the camera.")
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Camera', frame)

        # Click the 'c' key to capture image
        if cv2.waitKey(1) & 0xFF == ord('c'):
            image_count += 1
            image_filename = f'captured_image_{image_count}.jpg'
            cv2.imwrite(image_filename, frame)
            messagebox.showinfo("Image Captured", f"Image captured and saved as '{image_filename}'")

        # Click the 'v' key to exit the modal box
        key = cv2.waitKey(1) & 0xFF
        if key == ord('v') and not v_key_pressed:
            response = messagebox.askokcancel("Exit Confirmation", "Are you sure you want to exit?")
            if response:
                break
            else:
                v_key_pressed = True
        elif key != ord('v'):
            v_key_pressed = False
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images_with_notification()