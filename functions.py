import wikipedia
import urllib.request
import xmltodict
from rake_nltk import Rake


# Extract keywords from DM
def raker(words):
    r = Rake()
    r.extract_keywords_from_text(words)
    y = r.get_ranked_phrases()
    raked = []
    for x in y:
        raked.append(raked)
    return raked


# Search Wikipedia
def search(searchtext):
    x = wikipedia.summary(searchtext, sentences=1)
    wikipedia.WikipediaPage
    return x


# Get random cat gif
def cat():
    file = urllib.request.urlopen(
        'http://thecatapi.com/api/images/get?format=xml&size=full&category=funny&type=gif&results_per_page=1')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    pic = data['response']['data']['images']['image']['url']
    urllib.request.urlretrieve(pic, 'data/cat.gif')
