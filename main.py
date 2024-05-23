import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time
from threading import Thread
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class IoTDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Dashboard")
        self.root.geometry("1024x600")

        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        # Data storage for the charts
        self.temperature_data = []
        self.humidity_data = []
        self.pressure_data = []
        self.light_data = []
        
        # Create frames
        self.create_frames()

        # Create widgets
        self.create_widgets()

        # Start data simulation
        self.running = True
        self.start_data_simulation()

    def create_frames(self):
        self.frame1 = ctk.CTkFrame(master=self.root)
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.frame2 = ctk.CTkFrame(master=self.root)
        self.frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.frame3 = ctk.CTkFrame(master=self.root)
        self.frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.frame4 = ctk.CTkFrame(master=self.root)
        self.frame4.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.frame5 = ctk.CTkFrame(master=self.root)
        self.frame5.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure((0, 1), weight=1)

    def create_widgets(self):
        # Temperature and Humidity
        self.label_temp = ctk.CTkLabel(master=self.frame1, text="Temperature: -- °C", font=("Arial", 20))
        self.label_temp.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.label_humidity = ctk.CTkLabel(master=self.frame1, text="Humidity: -- %", font=("Arial", 20))
        self.label_humidity.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        # Device Status
        self.label_status = ctk.CTkLabel(master=self.frame2, text="Device Status: --", font=("Arial", 20))
        self.label_status.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.switch_status = ctk.CTkSwitch(master=self.frame2, text="Toggle Device", command=self.toggle_status)
        self.switch_status.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        # Captured Picture
        self.label_picture = ctk.CTkLabel(master=self.frame3, text="Camera")
        self.label_picture.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.image_label = ctk.CTkLabel(master=self.frame3)
        self.image_label.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        self.update_image()

        # Charts
        self.fig_temp, self.ax_temp = plt.subplots(figsize=(2, 2))
        self.ax_temp.set_title("Temperature Data")
        self.ax_temp.set_xlabel("Time")
        self.ax_temp.set_ylabel("Temperature (°C)")

        self.fig_humid, self.ax_humid = plt.subplots(figsize=(2, 2))
        self.ax_humid.set_title("Humidity Data")
        self.ax_humid.set_xlabel("Time")
        self.ax_humid.set_ylabel("Humidity (%)")

        self.fig_pressure, self.ax_pressure = plt.subplots(figsize=(2, 2))
        self.ax_pressure.set_title("Pressure Data")
        self.ax_pressure.set_xlabel("Time")
        self.ax_pressure.set_ylabel("Pressure (hPa)")

        self.fig_light, self.ax_light = plt.subplots(figsize=(2, 2))
        self.ax_light.set_title("Light Intensity Data")
        self.ax_light.set_xlabel("Time")
        self.ax_light.set_ylabel("Light Intensity (lux)")

        self.chart_temp_canvas = FigureCanvasTkAgg(self.fig_temp, master=self.frame4)
        self.chart_temp_canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.chart_humid_canvas = FigureCanvasTkAgg(self.fig_humid, master=self.frame4)
        self.chart_humid_canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.chart_pressure_canvas = FigureCanvasTkAgg(self.fig_pressure, master=self.frame4)
        self.chart_pressure_canvas.get_tk_widget().grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        self.chart_light_canvas = FigureCanvasTkAgg(self.fig_light, master=self.frame4)
        self.chart_light_canvas.get_tk_widget().grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        self.frame4.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        # Toggle Buttons
        self.toggle_buttons = []
        for i in range(6):
            toggle_button = ctk.CTkSwitch(master=self.frame5, text=f"Toggle {i+1}", command=lambda i=i: self.toggle_action(i))
            toggle_button.pack(pady=5, padx=5, side="left")
            self.toggle_buttons.append(toggle_button)

    def start_data_simulation(self):
        self.thread = Thread(target=self.simulate_data)
        self.thread.start()

    def simulate_data(self):
        while self.running:
            temp = random.uniform(20.0, 30.0)
            humidity = random.uniform(30.0, 70.0)
            pressure = random.uniform(900.0, 1100.0)
            light = random.uniform(100.0, 1000.0)
            status = random.choice(["Online", "Offline", "Error"])

            self.update_labels(temp, humidity, pressure, light, status)
            time.sleep(5)

    def update_labels(self, temp, humidity, pressure, light, status):
        self.temperature_data.append(temp)
        self.humidity_data.append(humidity)
        self.pressure_data.append(pressure)
        self.light_data.append(light)
        
        self.label_temp.configure(text=f"Temperature: {temp:.2f} °C")
        self.label_humidity.configure(text=f"Humidity: {humidity:.2f} %")
        self.label_status.configure(text=f"Device Status: {status}")
        
        self.update_charts()

    def update_charts(self):
        self.ax_temp.clear()
        self.ax_temp.plot(self.temperature_data, label='Temperature (°C)')
        self.ax_temp.set_title("Temperature Data")
        self.ax_temp.set_xlabel("Time")
        self.ax_temp.set_ylabel("Temperature (°C)")
        self.ax_temp.legend()
        self.chart_temp_canvas.draw()

        self.ax_humid.clear()
        self.ax_humid.plot(self.humidity_data, label='Humidity (%)', color='orange')
        self.ax_humid.set_title("Humidity Data")
        self.ax_humid.set_xlabel("Time")
        self.ax_humid.set_ylabel("Humidity (%)")
        self.ax_humid.legend()
        self.chart_humid_canvas.draw()
        
        self.ax_pressure.clear()
        self.ax_pressure.plot(self.pressure_data, label='Pressure (hPa)', color='green')
        self.ax_pressure.set_title("Pressure Data")
        self.ax_pressure.set_xlabel("Time")
        self.ax_pressure.set_ylabel("Pressure (hPa)")
        self.ax_pressure.legend()
        self.chart_pressure_canvas.draw()
        
        self.ax_light.clear()
        self.ax_light.plot(self.light_data, label='Light Intensity (lux)', color='purple')
        self.ax_light.set_title("Light Intensity Data")
        self.ax_light.set_xlabel("Time")
        self.ax_light.set_ylabel("Light Intensity (lux)")
        self.ax_light.legend()
        self.chart_light_canvas.draw()

    def update_data(self):
        temp = random.uniform(20.0, 30.0)
        humidity = random.uniform(30.0, 70.0)
        pressure = random.uniform(900.0, 1100.0)
        light = random.uniform(100.0, 1000.0)
        status = random.choice(["Online", "Offline", "Error"])
        self.update_labels(temp, humidity, pressure, light, status)

    def toggle_status(self):
        if self.switch_status.get() == 1:
            self.label_status.configure(text="Device Status: Online")
        else:
            self.label_status.configure(text="Device Status: Offline")

    def update_image(self):
        # Simulate captured image (replace with actual image capturing code)
        try:
            image = Image.open("assets/frame.jpg")  # Ensure this image exists or replace with actual path
            image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def toggle_action(self, toggle_index):
        state = "On" if self.toggle_buttons[toggle_index].get() == 1 else "Off"
        messagebox.showinfo("Toggle Switched", f"Toggle {toggle_index + 1} is {state}")

    def on_close(self):
        self.running = False
        self.thread.join()
        self.root.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = IoTDashboard(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
