#Start timer function
import time
import tkinter as tk
from tkinter import Text


print('''This is my timer, we will come back to this and turn it into a beautiful app 
                        or window, for now we get this...''')

#variables

seconds = 0
minutes = 0
'''
#Ask to begin
start = input("Lets start, shall we? (y/n)")

if start == "y":
    loop = True

while loop and minutes < 10: #CHANGE LATER FOR 90
    seconds +=1
    print(str(minutes) + " mins " + str(seconds) + " secs")
    #time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes += 1
    print(str(minutes) + " mins " + str(seconds) + " secs")
'''
def restart():
    minutes = 0
    start = True

def start():
    start = True

root = tk.Tk()

canvas = tk.Canvas(root, height = 950, width = 1820, bg="black") #CHANGE LATER ADD A 0 EACH
canvas.pack()

restartButton = tk.Button(root, text="Restart", padx=300, pady=100, bg="white", command=restart)
restartButton.place(x=1000, y=300)

startButton = tk.Button(root, text="Start", padx=300, pady=100, command=start)
startButton.place(x=100, y=300)

root.mainloop()