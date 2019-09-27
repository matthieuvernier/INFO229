import requests
from bs4 import BeautifulSoup
import time
import os
from pymongo import MongoClient
from datetime import datetime

### Script que recupera y escrapea las URLs de las últimas noticias del medio: elmundo.es - CADA 30 MINUTOS

DELAY=60*30 #30 minutos de espera
URL_BASE = "https://www.elmundo.es/ultimas-noticias.html"#URL que sirve de base para recuperar las urls de las noticias

while 1:
	
	#Conexión a la base de datos MONGO	
	client = MongoClient(os.environ['MONGO_URI'])
	db = client.sophia2
	collection_news = db.news
	
	#¿Cuál es la fecha de las ultimas noticias?
	date_news = datetime.now()
	date_news = date_news.strftime("%d/%m/%Y %H:%M:%S")
	print(date_news)	

	#Empezamos el scraping para recuperar las URLs de las últimas noticias
	r = requests.get(URL_BASE)

	#Buscamos los enlaces hacia las últimas noticias a partir del codigo HTML
	bs = BeautifulSoup(r.text, 'html5lib')
	h2_tags = bs.find_all('h2', attrs={"class":"mod-title"})

	urls_news=[] #arreglo de enlaces hacia últimas noticias

	for h2_tag in h2_tags:
		specific_a_tags = h2_tag.find_all('a')
		for a_tag in specific_a_tags:
			a_url = a_tag['href']
			#Si la url ya fue escrapeada antes, la dejamos de lado. Sino colocamos la url en la lista de las urls que escrapear	
			if collection_news.find({'url':a_url}).count() == 0:
				urls_news.append(a_url)

	#Extraemos el contenido de las noticias, esperando 3 segundos antes de consultar una nueva noticia
	news=[]

	for url_news in urls_news:
		time.sleep(3)
		r = requests.get(url_news)
		bs = BeautifulSoup(r.text, 'html5lib')
		try:		
			#TITLE
			div_title = bs.find('h1', attrs={'class':'ue-c-article__headline js-headline'})
			title_news = div_title.text

			#TEXT
			div_news = bs.find('div', attrs={'class':'ue-l-article__body ue-c-article__body'})
			p_tags = div_news.find_all('p')
			text_news=""
		    	
			for p_tag in p_tags:
			    	text_news = text_news+p_tag.text
		except:
			continue
    		
		#guardamos los datos en el arreglo "news"
		print(url_news)
		
		#news.append((url_news, date_news, title_news, text_news, "elmundo",r.text))
		dict_news = {}
		dict_news['url']=url_news
		dict_news['dateNews']=date_news
		dict_news['title']=title_news
		dict_news['text']=text_news
		dict_news['media']="elmundo"
		dict_news['raw_html']=r.text		

		doc = collection_news.insert_one(dict_news)
	
	#esperamos antes de hacer lo mismo
	time.sleep(DELAY)
