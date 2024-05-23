import serial
import time



class UART_Relay:
    def __init__(self):
        # Configure serial port
        self.ser = serial.Serial('/dev/ttyACM0', 115200)  # Change '/dev/ttyS0' to the appropriate serial port
        self.ser.flush()  # Clear input and output buffer
    def Relay_ON(self, id):
        print("UART ON", id)
        if id == 1:
            print("111111")
            char_to_send = '0'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if id == 2:
            print("222222")
            char_to_send = "2"
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if id == 3:
            char_to_send = '4'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if id == 4:
            char_to_send = '6'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if id == 5:
            char_to_send = '8'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
    def Relay_OFF(self, id):
        print("UART OFF", id)
        if id == 1:
            char_to_send = '1'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if id == 2:
            char_to_send = "3"
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if id == 3:
            char_to_send = '5'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if id == 4:
            char_to_send = '7'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if id == 5:
            char_to_send = '9'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
    def Solar_Panel(self, _cmd):
        if _cmd == 'D':
            char_to_send = 'C'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial
        if _cmd == 'U':
            char_to_send = 'D'
            self.ser.write(char_to_send.encode())  # Encode string to bytes and send via self.serial

