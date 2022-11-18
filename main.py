import cv2
import numpy as npVariable

# lê os valores dos pixels da imagem
img = cv2.imread('jaylo.jpg')

# ----------------------------------------------------------------------------
# INICIO DO CÓDIGO PARA MUDAR COR DA IMAGEM

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
green_img = cv2.merge([zeros, G, zeros])
# mostra janela com a imagem verde
cv2.imshow('Green shade', green_img)
# cria uma imagem com os valores de verde salvos
cv2.imwrite('jay_green.jpeg', green_img)


# mostra janela com a imagem vermelha
red_img = cv2.merge([zeros, zeros, R])
# salva uma array com valores de vermelho normais e valores
# verde e azul zerado
cv2.imshow('Red shade', red_img)
# cria uma imagem com os valores de vermelha salvos
cv2.imwrite('jay_red.jpeg', red_img)

# indica para esperar ser pressionado uma tecla para prosseguir
cv2.waitKey(0)
# ao finalizar o código fecha todas janelas
cv2.destroyAllWindows()

# ----------------------------------------------------------------------------
# INICIO DO CÓDIGO PARA INVERTER A IMAGEM

# mostra imagem original
cv2.imshow('original img', img)


# cria array com valores da imagem invertidos horizontalmente
img_flip_horizontal = cv2.flip(img, 1)
# mostra imagem com o eixo X invertido
cv2.imshow('flip horizontal', img_flip_horizontal)
# cria imagem com o eixo X invertido
cv2.imwrite('jay_flip_horizontal.jpeg', img_flip_horizontal)

# cria array com valores da imagem invertidos verticalmente
img_flip_vertical = cv2.flip(img, 0)
# mostra imagem com o eixo Y invertido
cv2.imshow('flip vertical', img_flip_vertical)
# cria imagem com o eixo Y invertido
cv2.imwrite('jay_flip_vertical.jpeg', img_flip_vertical)

# cria array com valores da imagem invertidos verticalmente e horizontalmente
img_flip_total = cv2.flip(img_flip_horizontal, 0)
# mostra imagem com os eixos X e Y invertidos
cv2.imshow('flip total', img_flip_total)
# cria imagem com os eixos X e Y invertidos
cv2.imwrite('jay_flip_total.jpeg', img_flip_total)

cv2.waitKey(0)
# ao finalizar o código fecha todas janelas
cv2.destroyAllWindows()
