import serial
from time import sleep

connection = serial.Serial("COM7", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
sleep(1)

user_input = 'r'
while(user_input != 'q'):
    user_input = input("What would you like to send:\n")
    
    connection.write(user_input.encode())

