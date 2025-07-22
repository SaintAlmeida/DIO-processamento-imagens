from image_processing import abrir_imagem, converter_para_cinza, redimensionar, salvar_imagem

# Abrir imagem
img = abrir_imagem("foto.jpg")

# Converter para escala de cinza
cinza = converter_para_cinza(img)

# Redimensionar
img_redimensionada = redimensionar(cinza, 200, 200)

# Salvar resultado
salvar_imagem(img_redimensionada, "resultado.jpg")
