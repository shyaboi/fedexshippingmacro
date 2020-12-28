from tkinter import Tk  
import keyboard

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print(Tk().clipboard_get())
            print('You Pressed A Key!')
            break  # finishing the loop
    except:Priscilla Contreras
        break  # 