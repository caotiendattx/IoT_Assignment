import cv2
import os
import time
import requests
# Create a VideoCapture object to capture frames from the camera stream

def split_image(image_path, output_directory):
    # Read the image
    image = cv2.imread(image_path)

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Define the number of rows and columns for splitting
    rows = 5
    cols = 7

    # Calculate the height and width of each sub-image
    sub_height = height // rows
    sub_width = width // cols

    # Counter for naming the output images
    image_count = 1

    # Iterate over rows and columns to split the image
    for r in range(rows):
        for c in range(cols):
            # Define the region of interest (ROI)
            y1 = r * sub_height
            y2 = (r + 1) * sub_height
            x1 = c * sub_width
            x2 = (c + 1) * sub_width

            # Crop the ROI
            sub_image = image[y1:y2, x1:x2]

            # Save the sub-image
            output_path = os.path.join(output_directory, f"sub_image_{image_count}.jpg")
            cv2.imwrite(output_path, sub_image)

            # Increment the image count
            image_count += 1

def get_image():
    cap = cv2.VideoCapture('rtsp://admin:ACLAB2023@172.28.182.165/ISAPI/Streaming/channels/1')
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Check if frame was successfully read
    if not ret:
        print("Error: Unable to capture frame.")
    frame = cv2.resize(frame, (640, 480))  # Adjust resolution as needed

    cv2.imwrite(f'./assets/frame.jpg', frame)

    input_image_path = "./assets/frame.jpg"
    output_directory = "./assets/output_images"

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Split the image into 40 smaller images
    #split_image(input_image_path, output_directory)
    cap.release()

def get_image_run():
    while True:
        get_image()
        time.sleep(5)



class Controller_Camera():
    def __init__(self):
        self.url = "https://admin:ACLAB2023@172.28.182.165/ISAPI/PTZCtrl/channels/1/continuous"
        self.headers = {
            "accept": "application/xml",
            "content-type": "application/xml"
        }
        

    def rotate_camera_right(self):
        data = '''
        <?xml version="1.0" encoding="UTF-8"?>
        <PTZData >
        <pan>20</pan>
        <tilt>0</tilt>
        </PTZData>
        '''
        response = requests.put(self.url, headers=self.headers, data=data, verify=False)
        print(response.text)
    
    def rotate_camera_left(self):
        data = '''
        <?xml version="1.0" encoding="UTF-8"?>
        <PTZData >
        <pan>-20</pan>
        <tilt>0</tilt>
        </PTZData>
        '''
        response = requests.put(self.url, headers=self.headers, data=data, verify=False)
        print(response.text)

    def rotate_stop_camera(self):
        data = '''
        <?xml version="1.0" encoding="UTF-8"?>
        <PTZData >
        <pan>0</pan>
        <tilt>0</tilt>
        </PTZData>
        '''
        response = requests.put(self.url, headers=self.headers, data=data, verify=False)
        print(response.text)


control_cam = Controller_Camera()
# while True:
#     input_key = input("Press from keyboard as your button in your app: ")
#     # 'r' => rotate right
#     # 'l' => rotate left
#     # 's' => stop
#     if input_key == 'r':
#         control_cam.rotate_camera_right()
#     elif input_key == 'l':
#         control_cam.rotate_camera_left()
#     elif input_key == 's':
#         control_cam.rotate_stop_camera()
#     else:
#         break


# get_image()