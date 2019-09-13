import requests
from bs4 import BeautifulSoup
import time
#import mysql.connector

#CONFIGURAMOS VARIABLES GLOBALES: BASE DE DATOS, URL QUE SCRAPEAR
MYSQL_HOST = "localhost"
MYSQL_PASSWORD = "root"
MYSQL_USER = "root"

URL = "https://www.elmundo.es/ultimas-noticias.html"


#Empezamos el scraping
r = requests.get(URL)

#Buscamos los enlaces hacia las últimas noticias a partir del codigo HTML
bs = BeautifulSoup(r.text, 'html5lib')
h2_tags = bs.find_all('h2', attrs={"class":"mod-title"})

enlaces=[] #arreglo de enlaces hacia últimas noticias

for h2_tag in h2_tags:
	specific_a_tags = h2_tag.find_all('a')
	for a_tag in specific_a_tags:
		print(a_tag['href'])
		enlaces.append(a_tag['href'])

#Extraemos el contenido de las noticias, esperando 2 segundos antes de consultar una nueva noticia
noticias=[]

for enlace in enlaces:
	time.sleep(2)r = requests.get(enlace)
	bs = BeautifulSoup(r.text, 'html5lib')
	div_noticia = bs.find('div', attrs={'class':'ue-l-article__body ue-c-article__body'})
	p_tags = div_noticia.find_all('p')
	texto_noticia=""
    	try:
        	for p_tag in p_tags:
            	texto_noticia = texto_noticia+p_tag.text
        except:
        	continue    	
	noticias.append((enlace,texto_noticia))

#Almacenamos el resultado del scraping en una base de datos MySQL
#db_connection = mysql.connector.connect(user=MYSQL_USER,host=MYSQL_HOST,password=MYSQL_PASSWORD)
#cursor = db_connection.cursor()

#...
