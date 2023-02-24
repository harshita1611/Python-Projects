import pyautogui
import time
import random
import string
num_of_message = int(input())

time.sleep(5)

for i in range(num_of_message):
    content_of_message = ''.join(random.choices(string.ascii_lowercase, k=5))
    pyautogui.write(content_of_message)
    pyautogui.press("Enter")
