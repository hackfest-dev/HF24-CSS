import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading
import webbrowser

def display_webpage():
    webbrowser.open("https://www.example.com")

def update_frame():
    _, frame = cap.read()  # Read frame from the camera

    # Convert frame to RGB format for displaying in Tkinter
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert frame to PIL Image format
    image = Image.fromarray(frame)

    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)

    # Update the label with the new photo
    label.config(image=photo)
    label.image = photo

    # Repeat after 10 milliseconds
    label.after(10, update_frame)

# Initialize the camera
cap = cv2.VideoCapture(0)

# Create the Tkinter app
app = tk.Tk()
app.title("Camera Feed")

# Create a label to display the camera feed
label = tk.Label(app)
label.pack()

# Start updating the frame
update_frame()

# Open the webpage in an external browser
web_thread = threading.Thread(target=display_webpage)
web_thread.start()

# Start the Tkinter main loop
app.mainloop()

# Release the camera when finished
cap.release()
