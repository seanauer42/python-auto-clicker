import time
import ctypes

# This is used to access Windows window API and is used a lot. I think it would be BS to type it every time
bs = ctypes.windll.user32

# This is the function that actually clicks the mouse. 2 is mouse down, 4 is mouse up
def click():
    bs.mouse_event(2,0,0,0,0)
    bs.mouse_event(4,0,0,0,0)


# This will continue to click until you specifically tell it to stop with Ctrl+c or closing the python window
while(True):
    click()
    time.sleep(0.6)
