import cv2
import tkinter as tk
from tkinter import messagebox

def capture_images_with_rectangle():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return
    slip_count = 0

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
        slips = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in slips:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Camera', frame)

        # Capture an image when 'c' is pressed
        if cv2.waitKey(1) & 0xFF == ord('c'):
            slip_count += 1
            slip_filename = f'captured_PDF_{slip_count}.jpg'
            cv2.imwrite(slip_filename, frame)
            print(f"Image captured and saved as '{slip_filename}'")
            messagebox.showinfo("Image Captured", f"Image captured and saved as '{slip_filename}'")

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
    capture_images_with_rectangle()