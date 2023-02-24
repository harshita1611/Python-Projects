import pyautogui
import time
num_of_messages = int(input())
message_content = input()
time.sleep(5)
for i in range(num_of_messages):
    pyautogui.write(message_content)
    pyautogui.press("enter")
