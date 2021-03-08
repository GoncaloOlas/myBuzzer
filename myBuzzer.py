#Start timer function
import time
import tkinter as tk
from tkinter import Text

def createTimerWindow():
    timerWindow = tk.Tk()

    canvas = tk.Canvas(timerWindow, height = 950, width = 1820, bg="black") #CHANGE LATER ADD A 0 EACH
    canvas.pack()

    restartButton = tk.Button(timerWindow, text="Restart", padx=300, pady=100, bg="white", command=start)
    restartButton.place(x=1000, y=300)

    startButton = tk.Button(timerWindow, text="Start", padx=300, pady=100, command=start)
    startButton.place(x=100, y=300)

    timerWindow.mainloop()
    return timerWindow

def start():
    seconds = 0
    minutes = 0
    start = True
    while start and minutes < 10: #CHANGE LATER FOR 90
        seconds +=1
        print(str(minutes) + " mins " + str(seconds) + " secs")
        #time.sleep(1)
        if seconds == 60:
            seconds = 0
            minutes += 1
        print(str(minutes) + " mins " + str(seconds) + " secs")
    
def main():
    timerWindow = createTimerWindow()
    timerWindow.mainloop()
if __name__ == '__main__':
        main()