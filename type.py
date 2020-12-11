import pyautogui
import time 
import re

name = 'first last'
address = 'num streetname rd'
zipcode = '99999'
# city = 'Houston'
phoneMessy = '5555555555'
weight = '5'
ticket = 'WLC/SR555555'
email = 'email@email.com'






phone = re.sub('[^A-Za-z0-9]+', '', phoneMessy)

def down():
    pyautogui.hotkey('tab')

pyautogui.hotkey('alt', 'tab')
for _ in range(15):
    pyautogui.hotkey('backspace')

pyautogui.write(name) 

for _ in range(2):
    down()

pyautogui.write(address) 

for _ in range(2):
    down()


pyautogui.write(zipcode) 
down()

# time.sleep(.4)
# pyautogui.write(f'{city[0]}{city[1]}')

# time.sleep(.4)
# pyautogui.press('down')
# time.sleep(.4)
# pyautogui.press('return')

for _ in range(2):
    down()

time.sleep(1)
pyautogui.write(phone)

time.sleep(1)

for _ in range(26):
    down()

pyautogui.write(weight) 

for _ in range(3):
    down()

pyautogui.press('up')

down()

pyautogui.press('up')
pyautogui.press('up')

down()
down()

pyautogui.press('space')

for _ in range(7):
    down()

pyautogui.write(ticket)

for _ in range(7):
    down()
pyautogui.hotkey('enter')

time.sleep(.4)

for _ in range(6):
    down()

pyautogui.press('down')
pyautogui.press('down')

for _ in range(18):
    down()

pyautogui.write(email)

for _ in range(4):
    down()

pyautogui.press('space')
down()
pyautogui.hotkey('space')
down()
pyautogui.hotkey('space')

# for _ in range(14):
#     down()

input("Press Enter to continue...")
pyautogui.hotkey('alt', 'tab')

# pyautogui.hotkey('enter')

time.sleep(2)

# for _ in range(65):
#     down()

pyautogui.write(weight) 

down()
down()
down()

pyautogui.hotkey('enter')

for _ in range(5):
    pyautogui.press('up')

pyautogui.hotkey('enter')



down()

time.sleep(.6)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')



for _ in range(12):
    down()

pyautogui.write(ticket)


# for _ in range(8):
#     down()

# pyautogui.hotkey('enter')

# time.sleep(.6)

# for _ in range(4):
#     down()

# pyautogui.press('down')
# pyautogui.press('down')

for _ in range(21):
    down()

pyautogui.write(email)

for _ in range(4):
    down()
pyautogui.hotkey('space')
down()
pyautogui.hotkey('space')
down()
pyautogui.hotkey('space')
down()
# for _ in range(20):
#     down()

# pyautogui.hotkey('enter')


# time.sleep(4)

# for _ in range(20):
#     down()
# pyautogui.press('space')

# for _ in range(4):
#     down()

# pyautogui.hotkey('enter')
