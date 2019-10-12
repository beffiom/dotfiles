import urllib
import urllib.request
import sys
from bs4 import BeautifulSoup

titles = []
episodeTitles = []
i=(int(sys.argv[2])-1)

class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()

#read command argument for episode list src
# url = input("Enter sauce: ")
url = sys.argv[1]
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)

#scrape wiki and append each entry to array
for lel in soup.select('td[class="summary"]'):
	titles.append(lel.next_element.strip())

for title in titles:
    if '(' in titles[i]:
        episodeTitle = (titles[i].replace('"', '').split('(', 1)[0])[:-1]
    elif '/' in titles[i]:
        episodeTitle = (titles[i].replace('"', '').split('/', 1)[0])[:-1]
    else:
        episodeTitle = (titles[i].replace('"', ''))

    print(episodeTitle)
    # episodeTitles.append(episodeTitle)
    i+=1

# print(episodeTitles)
