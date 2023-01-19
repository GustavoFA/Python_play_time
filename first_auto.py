
# Olhar Selenium

import cv2 as cv
import pyautogui
import time
import keyboard
import numpy as np

def fun_tri_draw(x0, y0, x, y):

    dif_x = 5
    dif_y = 5

    pyautogui.mouseDown()

    while True:
        pyautogui.moveTo(x0+x, y0+y)
        time.sleep(0.01)
        x += dif_x
        if (y0+y) >= 636:
            dif_y = -5
        elif (y0+y) <= 436:
            dif_y = 5

        y += dif_y

        if x > 800 and y == 536:
            pyautogui.mouseUp()
            break

def fun_seno(x0, yo, x, y):

    dif_x = 5
    dif_y = 5

    pyautogui.mouseDown()

    while True:
        pyautogui.moveTo(x0 + x, y0 + np.sin(y))
        time.sleep(0.01)
        x += dif_x
        if (y0 + y) >= 636:
            dif_y = -5
        elif (y0 + y) <= 436:
            dif_y = 5

        y += dif_y**(np.pi)/773

        if x > 800 and y == 536:
            pyautogui.mouseUp()
            break


# Para não travar o códifo no começo
pyautogui.FAILSAFE = False


# Abrir Paint
pyautogui.press('win')
pyautogui.write('Paint')
pyautogui.press('enter')

# Tempo para respirar
time.sleep(2)
# Verifica se abriu o programa
while True:
    pos_paint = pyautogui.locateOnScreen('paint.png')
    if pos_paint:
        break

# Selecionar a caneta
pyautogui.moveTo(456, 154)
time.sleep(1)
pyautogui.click(button='left')
img_caneta = 'caneta.png'
pos_caneta = pyautogui.locateOnScreen(img_caneta)
pyautogui.moveTo(pos_caneta)
time.sleep(1)
pyautogui.click(button='left')

# Posicionar o cursor em uma posição central
x0 = 28
y0 = 536

x = 0
y = 0
pyautogui.moveTo(28, 536)


# Simular a função Triangular
fun_tri_draw(x0, y0, x, y)











