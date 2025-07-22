from setuptools import setup, find_packages

setup(
    name='image_processing',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow'
    ],
    author='Seu Nome',
    description='Pacote simples para processamento de imagens usando Pillow',
    url='https://github.com/seunome/image_processing',
    python_requires='>=3.6',
)
