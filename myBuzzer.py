#Start timer function
import time

print('''This is my timer, we will come back to this and turn it into a beautiful app 
                        or window, for now we get this...''')

#variables

seconds = 0
minutes = 0

#Ask to begin
start = input("Lets start, shall we? (y/n)")

if start == "y":
    loop = True

while loop and minutes < 90:
    seconds +=1
    print(str(minutes) + " mins " + str(seconds) + " secs")
    #time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes += 1
    print(str(minutes) + " mins " + str(seconds) + " secs")
