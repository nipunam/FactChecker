import wikipedia
from nltk.tokenize import sent_tokenize
import sys
import re

class WikiData:
    @staticmethod
    def preprocess_content(content):
        content = re.sub(r'[=]{2,} .* [=]{2,}', ' ', content)
        content = content.replace('\n','. ').replace('\r','. ')
        content = re.sub(r'\.+', ".", content)
        return content

    @staticmethod
    def get_sentence(entities):
        titles = WikiData.get_titles(entities)
        print("Search results")
        print(titles)
        sentences = []
        for title in titles:
            try:
                page = wikipedia.page(title)
            except wikipedia.exceptions.DisambiguationError as e:
                page = wikipedia.page(e.options[0])
            print("Sections...")
            content = page.content
            content = WikiData.preprocess_content(content)
            # TODO : Remove section heading which starts and ends with ===.
            sentences.extend(sent_tokenize(content))
        print("Sentences..")
        print(sentences)
        return sentences

    @staticmethod
    def get_titles(entities):
        titles = []
        for entity in entities:
            titles.extend(wikipedia.search(entity, results=1))
        titles = WikiData.unique_list(titles)
        return titles

    @staticmethod
    def unique_list(l):
        ulist = []
        [ulist.append(x) for x in l if x not in ulist]
        return ulist

if __name__ == "__main__":
    WikiData.get_sentence(["India", "what is biggest city in India?"])
