#!/bin/python3

from PIL import Image

# Abre uma imagem existente
imagem_original = Image.open("My_shoe.jpg")

# Redimensiona a imagem para 300x300 pixels
imagem_redimensionada = imagem_original.resize((300, 300))

# Salva a imagem redimensionada
imagem_redimensionada.save("My_shoe_redimensionado.jpg")

# Fecha a imagem original
imagem_original.close()

