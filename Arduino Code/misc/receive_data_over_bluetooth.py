import serial

from time import sleep

import json

#connection = serial.Serial("COM8", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
connection = serial.Serial("COM7", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
user_input = 'n'

counter = 0


#while(user_input != 'y'):
while(counter < 200):

    #res = connection.read()
    res = connection.read_all()
    #print("receieved ", res, " decoded: ",res.decode('utf-8'), " \n")
    
    #print("receieved ", res.hex(), " decoded: ",res, " \n")
    if len(res) > 0:
        #json_string = res.decode('utf-8')
        #json_data = json.loads(json_string)
        try:
            json_data2 = json.loads(res.decode(json.detect_encoding(res)))
        except:
            continue
        
        print("json_data2: ")
        print(json.dumps(json_data2, indent=2))
        
        print(json_data2["acceleration_y"])
        print(json_data2["acceleration"]["z"])
    
    
    sleep(0.15)
    #user_input = input("Would you like to quit? if so please enter 'y' :\n")
    
    
    
    