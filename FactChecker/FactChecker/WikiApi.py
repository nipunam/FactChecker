import requests
from WikiData import WikiData
from nltk.tokenize import sent_tokenize

class WikiApi(object):
    """description of class"""
    # https://en.wikipedia.org/w/api.php?action=query&format=json&prop=cirrusdoc&titles=Hyderabad
    url = "https://en.wikipedia.org/w/api.php"
    @staticmethod
    def get_sentence(title):
        try:
            params = { 'action' : 'query', 'format': 'json', 'prop': 'cirrusdoc', 'titles': title }
            response = requests.get(WikiApi.url, params)
            data = response.json()
            pages = data["query"]["pages"]
            first_page = next(iter(pages))
            #print(pages[first_page])
            content = pages[first_page]["cirrusdoc"][0]["source"]["text"]
            #print(content)
            sentences = sent_tokenize(content)
            return sentences
        except:
            sentences = WikiData.get_sentence(entity)
            return sentences

if __name__ == '__main__':
    WikiApi.get_sentence("Hyderabad")