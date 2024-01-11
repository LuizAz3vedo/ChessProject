import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Define as imagens do carrossel
image1 = '../assets/teste1.jpg'
image2 = '../assets/jeet-dhanoa-BVM9Q6Qfy00-unsplash.jpg'
image3 = '../assets/kobus-yssel-Wct--ZoyReM-unsplash.jpg'
image4 = '../assets/pranjall-kumar-s-QQu6h1pMk-unsplash.jpg'

# Tamanho fixo para todas as imagens
fixed_image_size = {"width":"100%","height": '538px', 'object-fit': 'cover', "imgClassName": ""}

# Define o layout do carrossel
carousel = dbc.Carousel(
    items=[
        {"key": "image1", "src": image1, "img_style": fixed_image_size}, 
        {"key": "image2", "src": image2, "img_style": fixed_image_size},
        {"key": "image3", "src": image3, "img_style": fixed_image_size},
        {"key": "image4", "src": image4, "img_style": fixed_image_size}
    ],
    controls=True,
    indicators=True,
    
    interval=2000,  # Tempo de transição entre os slides (em milissegundos)
    style={'margin-top': '1rem', 'width': '100%', 'height': '100%'},  # Ajuste a altura desejada aqui
    className="carousel-container"
)


