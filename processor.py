from PIL import Image

def abrir_imagem(caminho):
    """Abre uma imagem e retorna o objeto PIL.Image"""
    return Image.open(caminho)

def converter_para_cinza(imagem):
    """Converte uma imagem para escala de cinza"""
    return imagem.convert("L")

def redimensionar(imagem, largura, altura):
    """Redimensiona a imagem para a largura e altura especificadas"""
    return imagem.resize((largura, altura))

def salvar_imagem(imagem, caminho):
    """Salva a imagem no caminho especificado"""
    imagem.save(caminho)
