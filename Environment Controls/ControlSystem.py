import tkinter as tk
import RPi.GPIO as GPIO
import time
from pygame import mixer
import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

root = tk.Tk()
root.title('Smart Bed Alarm')

def SetAlarm(alarm):
  alarmtime = alarm
  if(alarmtime != "::"):
    alarmclock(alarmtime)

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime != "::"):
        alarmclock(alarmtime)

def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now == alarmtime:
            print("Time to wake up!")
            mixer.init()
            mixer.music.load('Berliner Philharmoniker,Ludwig van Beethoven,Herbert von Karajan - Symphony No. 5.mp3')
            mixer.music.play()
            GPIO.output(18, GPIO.HIGH)
            time.sleep(40)
            GPIO.output(18, GPIO.LOW)
            mixer.fadeout()
            break

hrs=tk.StringVar()
mins=tk.StringVar()
secs=tk.StringVar()

greet=tk.Label(root, font = ('arial', 20, 'bold'), text = 'Smart Bed System Alarm').grid(row = 1, columnspan = 3)

hrbtn=tk.Entry(root, textvariable=hrs, width=5, font=('arial', 20, 'bold'))
hrbtn.grid(row=2, column=1)

minbtn=tk.Entry(root, textvariable=mins, width=5, font=('arial', 20, 'bold'))
minbtn.grid(row=2, column=2)

secbtn=tk.Entry(root, textvariable=secs, width=5, font=('arial', 20, 'bold'))
secbtn.grid(row=2, column=3)

setbtn=tk.Button(root, text="Set Alarm", command=setalarm, bg="black", fg="white", font=('arial', 20, 'bold'))
setbtn.grid(row=4, columnspan=3)



tk.mainloop()
