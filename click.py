import time
import ctypes
from typing import Optional

poo = input("Time? ")
u32 = ctypes.windll.user32

#Get the foreground window in the first place
hWnd = u32.GetForegroundWindow()
length = u32.GetWindowTextLengthW(hWnd)
buf = ctypes.create_unicode_buffer(u32.GetWindowTextLengthW(u32.GetForegroundWindow()) + 1)

#get the foreground window and return the title of the window
def getForegroundWindowTitle() -> Optional[str]:
	hWnd = u32.GetForegroundWindow()
	length = u32.GetWindowTextLengthW(hWnd)
	buf = ctypes.create_unicode_buffer(u32.GetWindowTextLengthW(u32.GetForegroundWindow()) + 1)
	u32.GetWindowTextW(hWnd, buf, length +1)
	if buf.value:
		return buf.value
	else:
		return "None"

#While powershell is the top window, tell the user to select a different window
active_window = getForegroundWindowTitle()
while "PowerShell" in active_window:
	print("click on the training window.")
	active_window = getForegroundWindowTitle()
	time.sleep(.6)

#click every poo amount of time until the active window changes
while(True):
	a = getForegroundWindowTitle()
	if a == active_window:
		print("click")
		ctypes.windll.user32.mouse_event(2,0,0,0,0)
		ctypes.windll.user32.mouse_event(4,0,0,0,0)
		#time.sleep(.6)
		time.sleep(float(poo))
	else:
		break
