from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p') # or soup.p
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

# extracting a tag's attributes by treating it like a dict

first_paragraph_id = soup.p['id'] # raises keyError if no 'id'
first_paragraph_id2 = soup.p.get('id') # returns None if no 'id'

# to get multiple tags at once

all_paragraphs = soup.find_all('p') # or just soap('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

# getting tags with a specific class

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p') if 'important' in p.get('class', [])]
