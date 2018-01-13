# Merci Andras !

import requests
from lxml import html

my_page = requests.get('https://twitter.com/emmanuelmacron')
htmlpage = html.fromstring(my_page.content)
followers = htmlpage.xpath('//@data-count')

print(followers[2])