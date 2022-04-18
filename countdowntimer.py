from tkinter import *
import time
import winsound
import threading
duration = 1000
freq = 440

# This is used to to increase the minutes or seconds time settings
def up(countvariable, limit:bool):
    if limit is True: # for seconds
        if countvariable["text"] != "59":
            current = int(countvariable["text"]) + 1
            fixed_current = str(current) if len(str(current)) == 2 else "0" + str(current)
            countvariable["text"] = fixed_current
        else:
            countvariable["text"] = "00"
    else: # for minutes
        if countvariable["text"] != "99":
            current = int(countvariable["text"]) + 1
            fixed_current = str(current) if len(str(current)) == 2 else "0" + str(current)
            countvariable["text"] = fixed_current
        else:
            countvariable["text"] = "00"

#this is to decrease the minutes or seconds time settings
def down(countvariable, limit:bool):
    if countvariable["text"] != "00":
        current = int(countvariable["text"]) - 1
        fixed_current = str(current) if len(str(current)) == 2 else "0" + str(current)
        countvariable["text"] = fixed_current
    else:
        countvariable["text"] = "59" if limit is True else "99"

# This is used to pause the timer and used on the start/stop button
def Stop(count, minutes, seconds):
    global running
    running = False
    global startbutton
    startbutton = Button(count, width=6,text="Start", command=lambda:start(count, minutes, seconds))
    startbutton.place(x=50, y=140)

# this is used to reset the timer to what the user put after the timer has reached 0 or when user clicked the reset button
def reset(count, minutes, seconds, times_up: bool) -> None:
    global counting_minute
    global counting_second
    global running
    global startbutton
    startbutton = Button(count, width=6, text="Start", command=lambda: start(count, minutes, seconds))
    startbutton.place(x=50, y=140)
    running = False
    startbutton["state"] = "disabled"
    if times_up is True:
        winsound.Beep(440, 3000)  # freq, duration (milliseconds)
    counting_minute["text"], counting_second["text"] = minutes, seconds
    startbutton["state"] = "normal"

# used to close the countdown timer after it is done
def on_closing(var):
    global running
    running = False
    var["state"] = "normal"
    countdown.destroy()

# this is used to start the countdown timer when the user click the start button both on the main GUI and the timer GUI
def start(count, minutes, seconds):
    global running
    running = True
    global startbutton
    startbutton = Button(count, width=6,text="Stop", command=lambda:Stop(count, minutes, seconds))
    startbutton.place(x=50, y=140)
    thread_count = threading.Thread(target=counting, daemon=True, args=(count, minutes, seconds))
    thread_count.start()

def counting(count, minutes, seconds):
    while running:
        global counting_minute
        global counting_second
        new_second = str(int(counting_second["text"]) - 1) if int(counting_second["text"]) - 1 >= 0 else str(59)
        new_minute = counting_minute["text"] if new_second != "59" else str(int(counting_minute["text"]) - 1)
        if new_minute == "-1":
            reset(count, minutes, seconds, times_up = True)
            break
        new_second, new_minute = new_second if len(new_second) == 2 else "0" + str(new_second), new_minute if len(new_minute) == 2 else "0" + str(new_minute)
        counting_minute["text"] = new_minute
        counting_second["text"] = new_second
        count.update()
        time.sleep(1)


# this is used to start the timer GUI once the user clicked start on the main GUI
def starttimer(var, minutes, seconds):
    var["state"] = "disabled"
    global countdown
    countdown = Tk()
    countdown.title("Counting down!")
    countdown.geometry("300x200")
    global counting_minute
    global counting_second
    counting_minute = Label(countdown, text=minutes, font=("Verdana bold", 35))
    counting_minute.place(x=40, y=50)
    counting_second = Label(countdown, text=seconds, font=("Verdana bold", 35))
    counting_second.place(x=180, y=50)
    middle = Label(countdown, text=":", font=("Verdana bold", 35)).place(x=135, y=50)
    global startbutton
    startbutton = Button(countdown, width=6,text="Start", command=lambda:start(countdown, minutes, seconds))
    startbutton.place(x=50, y=140)
    resetbutton = Button(countdown, width=6, text="Reset", command=lambda:reset(countdown, minutes, seconds, times_up = False)).place(x=190, y=140)
    countdown.protocol("WM_DELETE_WINDOW", lambda: on_closing(var))
    start(countdown, minutes, seconds)
    countdown.mainloop()







