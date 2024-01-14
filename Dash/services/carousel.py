import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Define as imagens do carrossel
image1 = '../assets/teste1.jpg'
image2 = '../assets/teste1.jpg'
image3 = '../assets/kobus-yssel-Wct--ZoyReM-unsplash.jpg'
image4 = '../assets/pranjall-kumar-s-QQu6h1pMk-unsplash.jpg'

# Tamanho fixo para todas as imagens
fixed_image_size = {'height': '300px', 'width': '100%'}

# Define o layout do carrossel
carousel = dbc.Carousel(
    items=[
        {"key": "image1", "src": image1},
        {"key": "image2", "src": image2},
        {"key": "image3", "src": image3},
        {"key": "image4", "src": image4}
    ],
    controls=True,
    indicators=True,
    interval=2000,  # Tempo de transição entre os slides (em milissegundos)
    style={'margin-top': '1rem', 'width': '100%', 'height': '100%'},  # Ajuste a altura desejada aqui
    className="carousel-container"
)


