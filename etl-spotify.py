#primeiro precisa instalar a biblioteca spotipy
#pip install spotipy

import pandas as pd

import spotipy

from spotipy.oauth2 import SpotifyOAuth

#autenticacao da api do spotify
client_id_spotify = ''
client_secret_spotify = ''
client_uri_spotify = 'http://localhost'

#digo as permissões que eu quero da minha conta
scp = 'user-top-read, user-read-recently-played'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id_spotify, client_secret= client_secret_spotify, redirect_uri= client_uri_spotify, scope= scp, open_browser= False))

#acessando as 5 musicas mais recentes
recent_songs = sp.current_user_recently_played(limit = 5)

musicas_recente = {}
nome_artista = []
nome_musica = []

#armazenando os dados da música (e seus artistas) recentemente tocadas
for itens in recent_songs['items']:
  nome_musica.append(itens['track']['name'])
  for info in itens['track']['album']['artists']:
    nome_artista.append(info['name'])

musicas_recentes = {'musica': nome_musica, 'artista': nome_artista}

#print(musicas_recentes)

#convertendo o dicionario para dataframe do pandas
musicas_recentes_df = pd.DataFrame.from_dict(musicas_recentes)

print(musicas_recentes_df)

#acessando as 5 musicas mais tocadas (padrao medium_term; aproximadamente 6 meses)
top = sp.current_user_top_tracks(limit= 5)

mais_ouvidas = {}
nome_do_artista = []
nome_da_musica = []

#armazenando as musicas e seus artistas
for itens in top['items']:
  nome_da_musica.append(itens['name'])
  for info in itens['album']['artists']:
    nome_do_artista.append(info['name'])

mais_ouvidas = {'musica': nome_da_musica, 'artista': nome_do_artista}

#print(mais_ouvidas)

mais_ouvidas_df = pd.DataFrame.from_dict(mais_ouvidas)

print(mais_ouvidas_df)