import pyautogui
import time 

name = 'Celeste Larsen'
address = '13725 cambury dr apt 412'
zipcode = '77014'
city = 'Houston'
phone = '2542692958'
weight = '20'
ticket = 'HUM/SR2764272'
email = 'Celestelarsen12@gmail.com'


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

time.sleep(.5)

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

for _ in range(14):
    down()

pyautogui.hotkey('enter')

time.sleep(4)

for _ in range(65):
    down()

pyautogui.write(weight) 

down()
down()
down()

pyautogui.hotkey('enter')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.hotkey('enter')



down()

time.sleep(.2)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')



for _ in range(12):
    down()

pyautogui.write(ticket)

for _ in range(8):
    down()

pyautogui.hotkey('enter')

time.sleep(.2)

for _ in range(4):
    down()

pyautogui.press('down')
pyautogui.press('down')

for _ in range(15):
    down()

pyautogui.write(email)

for _ in range(20):
    down()

pyautogui.hotkey('enter')


time.sleep(4)

for _ in range(20):
    down()
pyautogui.press('space')

# for _ in range(4):
#     down()

# pyautogui.hotkey('enter')
