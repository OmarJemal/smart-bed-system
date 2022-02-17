import time
import playsound
import datetime


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Wake Up")
        playsound.playsound(
            "./Berliner Philharmoniker,Ludwig van Beethoven,Herbert von Karajan - Symphony No. 5.mp3")
        break


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Invalid time format! Please try again"
    else:
        if int(alarm_time[0:2]) > 24:
            return "Invalid HOUR format! Please try again"
        elif int(alarm_time[3:5]) > 59:
            return "Invalid Minute format! Please try again"
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again"
        else:
            return "ok"

def actualTime():
    alarm_time = input("Enter time in 'HH:MM:SS' format: ")
    validate = validate_time(alarm_time)
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}")
        alarm(alarm_time)