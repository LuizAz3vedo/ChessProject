import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from googleapiclient.discovery import build
import base64
import requests
import dash_bootstrap_components as dbc
# Substitua 'SEU_API_KEY' pela sua chave de API do YouTube
API_KEY = 'AIzaSyDVOt7ApvJljXjlAsTlXccmWQPSMVGStas'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Lista de IDs de vídeos do YouTube
video_ids = [
    "j4fGOqmq_Ho",
    "mE1ipMq6B0I",
    "31aLdMNvGz0",
    # Adicione mais IDs conforme necessário
]

# Função para obter informações sobre vídeos usando a API do YouTube
def obter_informacoes_video(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    response = youtube.videos().list(part='snippet', id=video_id).execute()
    return response['items'][0]['snippet']

# Função para codificar uma imagem em base64 a partir de um URL
def codificar_imagem_url(imagem_url):
    imagem_codificada = base64.b64encode(requests.get(imagem_url).content).decode("utf-8")
    return f"data:image/jpeg;base64,{imagem_codificada}"

# Criação do carrossel
carousel_items = []
for video_id in video_ids:
    video_info = obter_informacoes_video(video_id)
    thumbnail_url = video_info['thumbnails']['high']['url']  # Use medium ou outra resolução desejada
    thumbnail_image = html.Img(src=codificar_imagem_url(thumbnail_url), style={'width': '100%'})
    thumbnail_link = html.A(thumbnail_image, href=f"https://www.youtube.com/watch?v={video_id}")
    carousel_items.append({'src': codificar_imagem_url(thumbnail_url), 'alt': f'Thumbnail {video_id}', 'link': thumbnail_link})
 # Substitua "#" pelo link desejado