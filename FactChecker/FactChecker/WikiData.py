import wikipedia
from nltk.tokenize import sent_tokenize
import sys

class WikiData:
	@staticmethod
	def get_sentence(entity):
		titles = wikipedia.search(entity, results=1)
		print("Search results");
		print(titles)
		sentences = []
		for title in titles:
			try:
				page = wikipedia.page(title)
			except wikipedia.exceptions.DisambiguationError as e:
				page = wikipedia.page(e.options[0])
			print("Sections...")
			content = page.content
			# TODO : Remove section heading which starts and ends with ===.
			sentences.extend(sent_tokenize(content))
		print("Sentences..")
		print(sentences)
		return sentences


if __name__ == "__main__":
	WikiData.get_sentence("India")
