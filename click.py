import time
import ctypes
import os
from typing import Optional

poo = input("Time? ")
u32 = ctypes.windll.user32
b = 0

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
print(active_window)
while "PowerShell" in active_window:
	print("click on the training window.")
	active_window = getForegroundWindowTitle()
	time.sleep(.6)

while "Python" in active_window:
	print("click on the training window.")
	active_window = getForegroundWindowTitle()
	time.sleep(.6)

#click every poo amount of time until the active window changes
if poo == "":
	poo = 0.6

def endless_click():
	global b
	while(True):
		a = getForegroundWindowTitle()
		if a == active_window:
			print("click", b)
			ctypes.windll.user32.mouse_event(2,0,0,0,0)
			ctypes.windll.user32.mouse_event(4,0,0,0,0)
			#time.sleep(.6)
			time.sleep(float(poo))
			b = b + 1
		else:
			break

def second():
	global b
	second = 0
	hour = 0
	minute = 0
	while(True):
		a = getForegroundWindowTitle()
		if a == active_window:
			# os.system('cls')
			if minute < 10 and second < 10:
				print(str(hour) + ":0" + str(minute) + ":0" + str(second))
			elif minute < 10:
				print(str(hour) + ":0" + str(minute) + ":" + str(second))
			elif second < 10:
				print(str(hour) + ":" + str(minute) + ":0" + str(second))
			else:
				print(str(hour) + ":" + str(minute) + ":" + str(second))
			ctypes.windll.user32.mouse_event(2,0,0,0,0)
			ctypes.windll.user32.mouse_event(4,0,0,0,0)
			#time.sleep(.6)
			time.sleep(float(poo))
			b = b + 1
			second = second + 1
			if b % 60 == 0:
				minute = minute + 1
				second = 0
			if minute == 60:
				hour = hour + 1
				minute = 0
		else:
			break

if float(poo) == 1.0:
	second()
else:
	endless_click()

