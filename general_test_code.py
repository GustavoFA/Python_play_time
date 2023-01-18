# Teste da Lib OpenCV

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os
import mouse
import pyautogui


# Versão do Open CV
#print(cv.__version__)

# ----------- IMAGEM ------------------

# Apresentar imagem de um diretório (sem nenhuma alteração)
# img = cv.imread('placa_1.jpg')
# cv.imshow("ORIGINAL", img)
# cv.waitKey(0)

# Apresentar imagem de um diretório (com alteração no cinza)
# img = cv.imread('placa_1.jpg', 20)
# cv.imshow("PARE c\ alteração", img)
# cv.waitKey(0)
# plt.imshow(img, cmap = 'gray')
# plt.show()

# ---------- EDGE -------------------------


# # Converter para escala de cinza (gray)
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # Blur para melhorar a detecção de borda
# img_blur = cv.GaussianBlur(img_gray, (3,3), 0)
#
#
# # Detector de borda Canny
# img_borda = cv.Canny(img, 150, 200) # 150 e 200
# canny = cv.Canny(image = img_blur, threshold1 = 150, threshold2 = 200)
# cv.imshow("CANNY", canny)
# cv.waitKey(0)
# cv.imshow("CANNY S/ BLUR", img_borda)
# cv.waitKey(0)
#
#
#
# # Detector de borda Sobel
# sobelx = cv.Sobel(src = img_blur, ddepth = cv.CV_64F, dx = 1, dy = 0, ksize = 5)
# sobely = cv.Sobel(src = img_blur, ddepth = cv.CV_64F, dx = 0, dy = 1, ksize = 5)
# sobelxy = cv.Sobel(src = img_blur, ddepth = cv.CV_64F, dx = 1, dy = 1, ksize = 5)
#
# cv.imshow('Sobel X', sobelx)
# cv.waitKey(0)
# cv.imshow('Sobel Y', sobely)
# cv.waitKey(0)
# cv.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv.waitKey(0)





# ----------- VÍDEO ------------------
# Pegar um vídeo salvo e apresentá-lo
# Não tenho nenhum vídeo aqui

# Captura de vídeo
# width = 640
# height = 480
#
# cap = cv.VideoCapture(0)
# cap.set(3, width)
# cap.set(4, height)
# cap.set(10, 150)
#
# while True:
#     success, img_cap = cap.read()
#
#     cv.imshow("Captura", img_cap)
#     cv.waitKey(0)
#     break



# ------------------ WINDOWS --------------------------

# Testando comandos do cmd

# Abrir cmd no modo ADM
#os.system('powershell start cmd -v runAs')

# Colocar um nome para o cmd aberto
#os.system('title TESTE')

# Apresenta as redes já conectadas
#os.system('netsh wlan show profile')

# Entrar em um site
#os.system('start https://www.eldorado.org.br/')



# ---------------- MOUSE --------------------

## Clicks do mouse
# mouse.click('right')
# mouse.click('left')

# # Obter posição
# print(mouse.get_position())

# Pegar um conjunto de posições do mouse
# move_mouse = mouse.record(button='left', target_types=('down',))
# print(move_mouse)

# ------ MOUSE and KEYBOARD ---------------


