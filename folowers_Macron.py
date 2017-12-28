# Merci Andres !

import requests
import lxml

my_page = requests.get('https://twitter.com/emmanuelmacron')
htmlpage = html.fromstring(pagestring.content)
followers = htmlpage.xpath('//@data-count')

print(followers[2])