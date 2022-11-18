import cv2
import numpy as npVariable

# lê os valores dos pixels da imagem
img = cv2.imread('jaylo.jpg')

# mostra janela com a imagem original
cv2.imshow('original img', img)

# separa os canais de cor da imagem em três diferentes arrays
B, G, R = cv2.split(img)

# cria uma imagem do mesmo tamanho que a original, mas com
# os valores zerados
zeros = npVariable.zeros(img.shape[: 2], dtype="uint8")

# salva uma array com valores de azul normais e valores
# vermelho e verde zerado
blue_img = cv2.merge([B, zeros, zeros])
# mostra janela com a imagem azul
cv2.imshow('Blue shade', blue_img)
# cria uma imagem com os valores de azul salvos
cv2.imwrite('jay_blue.jpeg', blue_img)

# salva uma array com valores de verde normais e valores
# vermelho e azul zerado
cv2.imshow('Green shade', cv2.merge([zeros, G, zeros]))
# mostra janela com a imagem verde
green_img = cv2.merge([zeros, G, zeros])
# cria uma imagem com os valores de verde salvos
cv2.imwrite('jay_green.jpeg', green_img)

# salva uma array com valores de vermelho normais e valores
# verde e azul zerado
cv2.imshow('Red shade', cv2.merge([zeros, zeros, R]))
# mostra janela com a imagem vermelha
red_img = cv2.merge([zeros, zeros, R])
# cria uma imagem com os valores de vermelha salvos
cv2.imwrite('jay_red.jpeg', red_img)

# indica para esperar ser pressionado uma tecla para prosseguir
cv2.waitKey(0)

# ao finalizar o código fecha todas janelas
cv2.destroyAllWindows()
