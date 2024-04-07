import cv2
import tkinter as tk
import webview
import threading

def display_webpage():
    webview.create_window("Webpage", "https://www.example.com")

def capture_camera():
    frame = cap.read()  # Read frame from the camera

    # Convert frame to RGB format for displaying in Tkinter
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert frame to PIL Image format
    image = Image.fromarray(frame)

    # Update the camera image in the Tkinter app
    camera_label.configure(image=image)
    camera_label.image = image
    camera_label.after(10, capture_camera)  # Repeat after 10 milliseconds


# Initialize the camera
cap = cv2.VideoCapture(0)

# Create the Tkinter app
app = tk.Tk()
app.title("Camera and Webpage App")

# Create a label to display the camera feed
camera_label = tk.Label(app)
camera_label.pack()

# Create a WebView to display the webpage
web_thread = threading.Thread(target=display_webpage)
web_thread.start()

# Set the URL of the webpage

# Start capturing the camera feed
capture_camera()

# Start the Tkinter main loop
app.mainloop()

# Release the camera and destroy the Tkinter app when finished
cap.release()
cv2.destroyAllWindows()
