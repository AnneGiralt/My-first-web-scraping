#Merci Liya pour récuperer un meilleur Xpath !
#Merci Quentin pour elephant_sql 
#Merci Maxime pour always_data

import requests
from lxml import html
import psycopg2
from getpass import getpass
import time

#A faire : décorateur sur la fonction get_data qui renvoie l'heure d'appel de la fonction !

def get_data():
	'''Cette fonction ouvre la page twitter de One direction, récupère le nombre d'abonnés et renvoie cette info + le moment de connection'''

	# Récuperer le nombre de followers :
	my_page = requests.get('https://twitter.com/onedirection')
	htmlpage = html.fromstring(my_page.content)
	followers = htmlpage.xpath('//a[@data-nav="followers"]/span/@data-count')

	# Heure de récupération des données :
	now = time.time()
	moment = time.strftime("%c",time.localtime(now))
	
	return (followers[0], moment)

def ecrire_table(nom_table, curseur):
	'''Cette fonction écrit dans la table nom_table à partir de la donnée du curseur, elle utilise la fontcion get_data'''

	for i in range(10):
	#On récupère les données :
		data = get_data()
		curseur.execute("INSERT INTO Nombre_followers (Followers, Date_prelevement) VALUES ({}, '{}')".format(data[0], data[1]))
		time.sleep(60)
		conn.commit()
	pass




conn = psycopg2.connect(dbname='cjcwnyod', host ='horton.elephantsql.com', user='cjcwnyod', password = 'nJk5tuqHerhab-I7XanbpNmVyCuWeTkb')
cursor = conn.cursor()


# Si beson on créer une nouvelle table : 
#cursor.execute("CREATE TABLE Nombre_followers (Followers int, Date_prelevement char(50))")

# On écrit les nouvelles données :
ecrire_table('Nombre_followers', cursor)


# On ferme !
cursor.close()
conn.close()
