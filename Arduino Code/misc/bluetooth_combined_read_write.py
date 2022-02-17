import serial

from time import sleep
import threading

connection = serial.Serial("COM7", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

user_input = 'r'


def read_bluetooth_serial():
    while(True):
        
        print(connection.read_all())
        res = connection.read()
        #print("receieved ", res, " decoded: ",res.decode('utf-8'), " \n")
        print("receieved ", res, " decoded: ",res.hex(), " \n")
        sleep(0.15)
        
def write_to_bluetooth_serial():
    global user_input
    while(user_input != 'q'):
        user_input = input("What would you like to send:\n")
        
        connection.write(user_input.encode())
        
        print(connection.read_all())
        
if __name__ == "__main__":
    read_thread = threading.Thread(target=read_bluetooth_serial)
    write_thread = threading.Thread(target=write_to_bluetooth_serial)
    
    read_thread.start()
    write_thread.start()
    
    read_thread.join()
    write_thread.join()

