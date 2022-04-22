import countdowntimer
from tkinter import *

# main function to execute the timer GUI
def main():
    global root
    root = Tk()
    root.title("Countdown Timer")
    root.geometry("300x150")
    root.resizable(0, 0)
    root.iconbitmap("countdowntimer.ico")
    running = False
    Textlbl = Label(root, text="Insert countdown time").place(x=100, y=0)
    Minuteslabel = Label(root, text="Minutes").place(x=40, y=30)
    Secondslabel = Label(root, text=" Seconds").place(x=180, y=30)
    Minuteslbl = Label(root, text="00", font=("Verdana bold", 35))
    Minuteslbl.place(x=20, y=50)
    Secondslbl = Label(root, text="00", font=("Verdana bold", 35))
    Secondslbl.place(x=160, y=50)
    minuteup = Button(root, width=5, text="^", command=lambda: countdowntimer.up(Minuteslbl, limit=False)).place(x=100, y=60)
    minutedown = Button(root, width=5, text="▼", command=lambda: countdowntimer.down(Minuteslbl, limit=False)).place(x=100, y=80)
    secondup = Button(root, width=5, text="^", command=lambda: countdowntimer.up(Secondslbl, limit=True)).place(x=240, y=60)
    seconddown = Button(root, width=5, text="▼", command=lambda: countdowntimer.down(Secondslbl, limit=True)).place(x=240, y=80)
    startcountdown = Button(root, text="Start", command=lambda: countdowntimer.starttimer(startcountdown, Minuteslbl["text"], Secondslbl["text"]))
    startcountdown.place(x=130, y=120)

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


"""
1) If you can, define the labels, button etc in a separate file and then import it. It would really clean up the main file.
2) If you open the timer as a new window, maybe you can utilize threads or something like that? Because the application works but it's quite laggy.
3) When you open the new window, make the timer start automatically. 
4) I personally really like to do this, I would suggest you define a main function and it is the first function to run and executes everything. You see this kind of stuff in languages like C/C++
5) Add short comments above functions that tell what it does.
"""
