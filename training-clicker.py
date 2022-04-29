import time
import ctypes

# This is used to expose the Windows API and would have to be typed a lot which would be BS
bs = ctypes.windll.user32

# This function clicks the mouse with 2 being button down, and 4 being button up. Also prints "click" to verify operation
def click():
        bs.mouse_event(2,0,0,0,0)
        bs.mouse_event(4,0,0,0,0)
        print("click")
       

# These are starting variables to move the mouse to. They were correct on the computer I was on at the time, 
# but different computers have different dimentions and aspect ratios so we need to manipulate them
x1 = 803
x2 = 950
y = 700

mouse_pos1 = "n"
mouse_pos2 = "n"

# Here is where you set the mouse position to click on the progress bar to move it to the end. Moves 5 pixels at a time so you can 
# get it as close to the end as possible. You can also just move the window to the correct spot.
while(mouse_pos1 != "y"):
        bs.SetCursorPos(x1, y)
        mouse_pos1 = input("is the first mouse position good? ([u]p, [d]own, [l]eft, [r]ight, [y]es)")
        match mouse_pos1:
                case "u":
                        y -= 5
                case "d":
                        y += 5
                case "l":
                        x1 -= 5
                case "r":
                        x1 += 5
                case _:
                        print("first position set")
                       

# Here is where you move the mouse to the "Next" button
while(mouse_pos2 != "y"):
        bs.SetCursorPos(x2, y)
        mouse_pos2 = input("is the second mouse position good? ([u]p, [d]own, [l]eft, [r]ight, [y]es)")
        match mouse_pos2:
                case "u":
                        y -= 5
                case "d":
                        y += 5
                case "l":
                        x2 -= 5
                case "r":
                        x2 += 5
                case _:
                        print("let's go!")
                       
                       
# This will continue to click those 2 spots until told to stop                       
while(True):
        bs.SetCursorPos(x1, y)
        click()
        time.sleep(1.5)
        bs.SetCursorPos(x2, y)
        click()
        time.sleep(0.6)
