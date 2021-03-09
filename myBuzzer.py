#Start timer function
import time
import tkinter as tk
from tkinter import Text

def start():
    seconds = 0
    minutes = 0
    start = True
    timerWindow.wm_state('iconic')
    while start and minutes < 90:
        seconds +=1
        print(str(minutes) + " mins " + str(seconds) + " secs")
        time.sleep(1)
        if seconds == 60:
            seconds = 0
            minutes += 1  
    timerWindow.attributes("-topmost", True)
    timerWindow.lift()
    timerWindow.wm_state('zoomed')

timerWindow = tk.Tk()
timerWindow.title("MY STUDYING TIMER")
timerWindow.state('zoomed')
canvas = tk.Canvas(timerWindow, height = 950, width = 1820, bg="black") 
canvas.pack()

startButton = tk.Button(timerWindow, text="Start", padx=300, pady=100, command=start)
startButton.place(x=600, y=350)

timerWindow.mainloop()
