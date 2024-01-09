from __future__ import division 
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, Dash
from pandas._libs import properties

from app import *
from components import navbardash
from services import carousel


df = pd.read_csv("Df\games.csv")
df['opening_name'] = df['opening_name'].str.split(':').str[0]
options_status = [
    {'label': 'Todos', 'value': 0},
    {'label': '0 - 400', 'value': 1},
    {'label': '400 - 800', 'value': 2},
    {'label': '800 - 1200', 'value': 3},
    {'label': '1200 - 1600', 'value': 4},
    {'label': '1600 - 2000', 'value': 5},
    {'label': '2000 - 2400', 'value': 6},
    {'label': '2400 - 2800', 'value': 7},
]
options_victory_status = [
    {'label': 'Todos', 'value': 0},
    {'label': 'Checkmate', 'value': 'mate'},
    {'label': 'Acabou o Tempo', 'value': 'outoftime'},
    {'label': 'Empate', 'value': 'draw'},
    {'label': 'Desistente', 'value': 'resign'},
]

# ↧ layout ↧ ========================================================================================
layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col([
            navbardash.header
        ], style={'padding': '0'})
    ]),
    dbc.Row([
        dbc.Card([
            html.P('Filtro por rating:'),
            dbc.RadioItems(
                id="radio_status",
                options=options_status,
                value=0,  # Define o valor padrão
                inline=True,
                labelCheckedClassName="text-success",
                inputCheckedClassName="border border-success bg-success",
            )
        ], style={'margin-top': '1rem', 'margin-left': '1rem'}),
        dbc.Card([
            html.P('Filtro por Status de Vitória:'),
            dbc.RadioItems(
                id="radio_victory_status",
                options=options_victory_status,
                value=0,  # Define o valor padrão
                inline=True,
                labelCheckedClassName="text-success",
                inputCheckedClassName="border border-success bg-success",
            )
        ], style={'margin-top': '1rem', 'margin-left': '1rem'}),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.P('Aberturas mais populares desconsiderando a variação:'),
                        dcc.Graph(
                            id='bar_popular_openings',
                            config={
                                "displayModeBar": True,
                                "displaylogo": False,
                                "modeBarButtonsToRemove": [
                                "pan2d", "select2d", "lasso2d", "zoomIn2d", 
                                "zoomOut2d", "autoScale2d", "orbitRotation"
                            ]
                            }
                        )
                    ], style={'height': '100%'})
                ], style={'margin-top': '1rem'}),
            ], md=8, style={'height': '100%'}),
            dbc.Col([
                html.Div(
                    carousel.carousel
                )
            ], md=4)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='pie'
                        )
                    ], style={'height': '80%'})
                ], style={'margin-top': '1rem'}),
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='dispersao'
                        )
                    ], style={'height': '80%'})
                ], style={'margin-top': '1rem'}),
            ], md=6),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='table'
                        )
                    ], style={'height': '80%'})
                ], style={'margin-top': '1rem'}),
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='mode'
                        )
                    ], style={'height': '80%'})
                ], style={'margin-top': '1rem'}),
            ], md=6),
        ])
    ])
], style={'padding': '0'})


# Função para filtrar o DataFrame
def get_filtered_df(selected_status, selected_victory_status):
    min_value, max_value, status_selected = 0, 9999, 'mate'

    if selected_status != 0:
        selected_option = next((opt for opt in options_status if opt['value'] == selected_status), None)
        if selected_option:
            min_value, max_value = map(int, selected_option['label'].split(' - '))

    if selected_victory_status != 0:
        selected_option_v = next((opt for opt in options_victory_status if opt['value'] == selected_victory_status), None)
        if selected_option_v:
            status_selected = selected_option_v['value']

    # Filtrar o DataFrame com base nos valores selecionados
    filtered_df = df[(df['black_rating'] >= min_value) & (df['black_rating'] <= max_value) & (df['victory_status'] == status_selected)]
    return filtered_df

# Callback para atualizar o gráfico
@app.callback(
    Output('bar_popular_openings', 'figure'),
    [Input('radio_status', 'value'),
     Input('radio_victory_status', 'value')]
)
def update_chart(selected_status, selected_victory_status):
    if selected_status != 0 or selected_victory_status != 0:
        filtered_df = get_filtered_df(selected_status, selected_victory_status)
        popular_openings = filtered_df['opening_name'].value_counts().head(10)
    else:
        popular_openings = df['opening_name'].value_counts().head(10)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=popular_openings.values,
            y=popular_openings.index,
            orientation='h',
            marker_color='#90D0EC',
            textposition='auto'
        )
    )

    fig.update_layout(
        title="Frequência das Aberturas Populares",
        xaxis_title="Frequência",
        yaxis_title="Aberturas",
        margin=dict(l=80, r=80, t=80, b=80),
        paper_bgcolor='#ecf0f1',
        plot_bgcolor='#ecf0f1',
        font=dict(family="Nova Square", size=12, color="#2c3e50"),
        showlegend=False,
    )

    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#bdc3c7')

    fig.update_layout(shapes=[
        dict(
            type='rect',
            xref='paper', yref='y',
            x0=0, x1=0.02, y0=0, y1=len(popular_openings) - 1,
            fillcolor='rgba(0,0,0,0)',
            opacity=0.9,
            line=dict(color='#95a5a6', width=0.5),
        )
    ])

    return fig
    
@app.callback(
    Output('pie', 'figure'),
    [Input('radio_status', 'value'),
     Input('radio_victory_status', 'value')]
)
def create_pie_chart(selected_status, selected_victory_status):
    # Configurações padrão
    min_value, max_value = 0, 9999

    if selected_status != 0 or selected_victory_status != 0:
        filtered_df = get_filtered_df(selected_status, selected_victory_status)
        popular_ratings = filtered_df['rated'].value_counts()
    else:
        popular_ratings = df['rated'].value_counts()

    # Criar o gráfico de pizza
    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels=['Partida com Rating', 'Partida sem Rating'],
            values=popular_ratings.values,
            marker=dict(colors=['#F5B041', '#90D0EC'], line=dict(color='#2c3e50', width=2)),  # Cores e borda
            textinfo='percent+label',
            hole=0.4,  # Adiciona um buraco no meio para um visual mais elegante
            pull=[0.2, 0],  # Expansão para destacar "Partida com Rating"
        )
    )

    # Adicionar legenda das cores no canto superior direito
    fig.update_layout(
        legend=dict(x=0.9, y=1.1),
    )

    fig.update_layout(
        title="Distribuição de Partidas Avaliadas",
        margin=dict(l=80, r=80, t=80, b=80),
        paper_bgcolor='#ecf0f1',  # Cor de fundo do gráfico
        plot_bgcolor='#ecf0f1',  # Cor de fundo do plot
        font=dict(family="Nova Square, sans-serif", size=12, color="#2c3e50"),  # Estilo da fonte
        showlegend=True,
    )

    return fig
    
@app.callback(
    Output('dispersao', 'figure'),
    [Input('radio_status', 'value'),
     Input('radio_victory_status', 'value')]
)
def create_dispersao_chart(selected_status, selected_victory_status):
    # Filtrar apenas partidas classificadas
    filtered_df = df[df['rated'] == True]

    if selected_status != 0 or selected_victory_status != 0:
        # Filtrar com base nos valores selecionados
        filtered_df = get_filtered_df(selected_status, selected_victory_status)
        
    # Extrair os nomes das aberturas até os dois pontos
    filtered_df['opening_name'] = filtered_df['opening_name'].apply(lambda x: x.split(':')[0])

    # Contar o número de jogos por abertura
    opening_counts = filtered_df['opening_name'].value_counts()

    # Selecionar as top 10 aberturas com mais jogos
    top_10_openings = opening_counts.head(10).index

    # Filtrar o DataFrame para incluir apenas as top 10 aberturas
    filtered_df = filtered_df[filtered_df['opening_name'].isin(top_10_openings)]

    # Calcular a taxa de vitórias para cada abertura em porcentagem
    opening_winrates = filtered_df.groupby('opening_name')['winner'].apply(lambda x: (x == 'black').mean() * 100 if 'black' in x.unique() else (x == 'white').mean() * 100)

    # Criar o gráfico de dispersão
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=opening_winrates.index,
            y=opening_winrates.values,
            mode='markers',
            marker=dict(
                size=10,
                color='#90D0EC',
                opacity=0.8
            ),
            hovertemplate='%{x}: %{y:.2f}%<extra></extra>'
        )
    )

    fig.update_layout(
        title="Taxa de Vitórias por Abertura",
        xaxis_title="Aberturas",
        yaxis_title="Taxa de Vitórias (%)",
        margin=dict(l=80, r=80, t=80, b=80),
        paper_bgcolor='#ecf0f1',  # Cor de fundo do gráfico
        plot_bgcolor='#ecf0f1',  # Cor de fundo do plot
        font=dict(family="Nova Square, sans-serif", size=12, color="#2c3e50"),  # Estilo da fonte
        showlegend=False,  # Não mostrar a legenda neste caso
    )

    # Adicionar linhas e grade horizontais
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#bdc3c7')

    return fig



@app.callback(
    Output('mode', 'figure'),
    [Input('radio_status', 'value'),
     Input('radio_victory_status', 'value')]
)
def create_waterfall_chart(selected_status, selected_victory_status):
    # Filtrar apenas partidas classificadas
    filtered_df = df

    if selected_status != 0 or selected_victory_status != 0:
        # Filtrar com base nos valores selecionados
        filtered_df = get_filtered_df(selected_status, selected_victory_status)

    # Contar o número de partidas por modo incremental
    increment_counts = filtered_df['increment_code'].value_counts()

    # Selecionar os cinco modos incrementais mais jogados
    top_5_increments = increment_counts.head(5).index

    # Filtrar o DataFrame para incluir apenas os cinco modos incrementais mais jogados
    filtered_df = filtered_df[filtered_df['increment_code'].isin(top_5_increments)]

    # Contar o número de vezes que cada incremento apareceu nos cinco mais jogados
    num_partidas_por_incremento = filtered_df['increment_code'].value_counts()

    # Criar o gráfico de cascata
    fig = go.Figure(go.Waterfall(
        name='Incremental Games',
        orientation='v',
        measure=["relative"] * 5 + ["total"],
        x=num_partidas_por_incremento.index.tolist() + ['Total'],
        textposition=["inside"] * 5 + ["inside"],
        text=num_partidas_por_incremento.tolist() + [num_partidas_por_incremento.sum()],
        y=num_partidas_por_incremento.tolist() + [0],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        increasing={"marker": {"color": '#F5B041'}},  # Cor para barras crescentes
        decreasing={"marker": {"color": '#90D0EC'}}  # Cor para barras decrescentes
    ))

    # Personalizar layout do gráfico
    fig.update_layout(
        title='Top 5 Modos de Incrementos mais Jogados',
        xaxis_title='Incremento',
        yaxis_title='Número de Jogos',
        font=dict(family="Nova Square, sans-serif", size=12, color="#2c3e50"),  # Tamanho e cor do título
        xaxis=dict(title_font=dict(size=12)),  # Tamanho do título do eixo x
        yaxis=dict(title_font=dict(size=12)),  # Tamanho do título do eixo y
        legend=dict(font=dict(size=12)),  # Tamanho da legenda
        paper_bgcolor='rgba(0,0,0,0)',  # Cor do fundo
        plot_bgcolor='rgba(0,0,0,0)',  # Cor do fundo do gráfico
    )

    return fig