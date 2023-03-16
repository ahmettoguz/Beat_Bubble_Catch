import pyautogui
import keyboard
import time
# import win32api
# import win32con

# def click(x, y):
#     win32api.SetCursorPos((x, y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

pyautogui.PAUSE = 0

print("Press < to start program")
keyboard.wait('<')
time.sleep(1)


while keyboard.is_pressed('<') == False:
    sc = pyautogui.screenshot()
    for x in range(530, 1390, 50):
        for y in range(340, 945, 50):
            if sc.getpixel((x, y))[1] >= 200:
                pyautogui.click(x, y)


print("Stopped")
