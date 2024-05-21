import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time
from threading import Thread

class IoTDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Dashboard")
        self.root.geometry("600x400")

        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        # Create frames
        self.create_frames()

        # Create widgets
        self.create_widgets()

        # Start data simulation
        self.running = True
        self.start_data_simulation()

    def create_frames(self):
        self.frame1 = ctk.CTkFrame(master=self.root)
        self.frame1.pack(pady=10, padx=10, fill="x", expand=True)

        self.frame2 = ctk.CTkFrame(master=self.root)
        self.frame2.pack(pady=10, padx=10, fill="x", expand=True)

        self.frame3 = ctk.CTkFrame(master=self.root)
        self.frame3.pack(pady=10, padx=10, fill="x", expand=True)

    def create_widgets(self):
        # Temperature and Humidity
        self.label_temp = ctk.CTkLabel(master=self.frame1, text="Temperature: -- °C", font=("Arial", 20))
        self.label_temp.pack(pady=10, side="left", padx=20)

        self.label_humidity = ctk.CTkLabel(master=self.frame1, text="Humidity: -- %", font=("Arial", 20))
        self.label_humidity.pack(pady=10, side="left", padx=20)

        # Device Status
        self.label_status = ctk.CTkLabel(master=self.frame2, text="Device Status: --", font=("Arial", 20))
        self.label_status.pack(pady=10, side="left", padx=20)

        self.switch_status = ctk.CTkSwitch(master=self.frame2, text="Toggle Device", command=self.toggle_status)
        self.switch_status.pack(pady=10, side="left", padx=20)

        # Captured Picture
        self.label_picture = ctk.CTkLabel(master=self.frame3, text="Camera")
        self.label_picture.pack(pady=10, side="left", padx=20)

        self.image_label = ctk.CTkLabel(master=self.frame3)
        self.image_label.pack(pady=10, side="left", padx=20)

        self.update_image()

        # Refresh Button
        self.button_refresh = ctk.CTkButton(master=self.root, text="Refresh", command=self.update_data)
        self.button_refresh.pack(pady=10)

    def start_data_simulation(self):
        self.thread = Thread(target=self.simulate_data)
        self.thread.start()

    def simulate_data(self):
        while self.running:
            temp = random.uniform(20.0, 30.0)
            humidity = random.uniform(30.0, 70.0)
            status = random.choice(["Online", "Offline", "Error"])

            self.update_labels(temp, humidity, status)
            time.sleep(5)

    def update_labels(self, temp, humidity, status):
        self.label_temp.configure(text=f"Temperature: {temp:.2f} °C")
        self.label_humidity.configure(text=f"Humidity: {humidity:.2f} %")
        self.label_status.configure(text=f"Device Status: {status}")

    def update_data(self):
        temp = random.uniform(20.0, 30.0)
        humidity = random.uniform(30.0, 70.0)
        status = random.choice(["Online", "Offline", "Error"])
        self.update_labels(temp, humidity, status)

    def toggle_status(self):
        if self.switch_status.get() == 1:
            self.label_status.configure(text="Device Status: Online")
        else:
            self.label_status.configure(text="Device Status: Offline")

    def update_image(self):
        # Simulate captured image (replace with actual image capturing code)
        try:
            image = Image.open("sample_image.png")  # Ensure this image exists or replace with actual path
            image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def on_close(self):
        self.running = False
        self.thread.join()
        self.root.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = IoTDashboard(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
