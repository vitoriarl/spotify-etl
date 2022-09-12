#!pip install spotipy --upgrade

#pip install mysql-connector-python

#importação das bibliotecas
#import psycopg2
#import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import mysql.connector

#declarando as variveis que vão armazenar o id, o segredo do spotify e a url para permitir o acesso
client_id_spotify = ''
client_secret_spotify = ''
client_url_spotify = 'http://localhost:8888'

#nesse momento só quero acessar as minhas informações das musicas mais ouvidas
scp = 'user-top-read'

#autenticação no spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id_spotify, client_secret= client_secret_spotify, redirect_uri= client_url_spotify, scope= scp, open_browser= False))

#requisitando as 10 mais ouvidas no padrão medium_term (aproximadamente 6 meses)
top_songs = sp.current_user_top_tracks(limit= 10)
#print(top_songs)

#eu só estou interessada no artista e no nome da música, por isso tenho que
#retirar os dados do dict top_songs
mais_ouvidas = {}
nome_do_artista = []
nome_da_musica = []

for itens in top_songs['items']:
  nome_da_musica.append(itens['name'])
  for info in itens['album']['artists']:
    nome_do_artista.append(info['name'])

#armazenando em um dict para futura visualização em gráfico
mais_ouvidas = {'musica': nome_da_musica, 'artista': nome_do_artista}

#print(mais_ouvidas)
#print(nome_do_artista)
#print(nome_da_musica)

#Conexão com o banco de dados MySQL fazendo o insert a partir de um stored procedure

contador2 = 0
con = mysql.connector.connect(user='', password='', host='', database='musicas')
if con.is_connected():
  cursor = con.cursor()
  while contador2 < len(nome_da_musica):
    cursor.callproc('inserir_musicas', (nome_da_musica[contador2], nome_do_artista[contador2],))
    contador2 = contador2 + 1
  for result in cursor.stored_results():
    print(result.fetchall())
  con.commit()

if con.is_connected():
  cursor.close()
  con.close()
  print('Conexão encerrada.')

#Alternativa se for trabalhar com postgresql
'''
con =  psycopg2.connect(user='', password='', host='', database='musicas')
cursor = con.cursor()
while contador2 < len(nome_da_musica):
    cursor.execute("CALL inserir_musicas(%s, %s);",(nome_da_musica[contador2], nome_do_artista[contador2]))
    contador2 = contador2 + 1
con.commit()
cursor.close
con.close
'''



