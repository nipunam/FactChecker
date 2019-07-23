import nltk
import gensim
import numpy as np
from nltk.corpus import stopwords
class SentenceSimilarity(object):
	model = gensim.models.KeyedVectors.load_word2vec_format('C:/Users/rapotham/Desktop/Word2Vec/GoogleNews-vectors-negative300.bin.gz', binary=True,limit =500000)  
	stops = set(stopwords.words('english'))
	@staticmethod
	def CosineSimilarity(vec1, vec2):
		score = 0.0
		for i in range(len(vec1)):
			score = score + vec1[i]*vec2[i]
		return score
	@staticmethod
	def GetVector(wordList, model):
		## remove the stopwords
		## Add the words
		## Divide by the number of words 
		## return the vector
		wordCount = 0
		vec = np.zeros(300)
		for word in wordList:
			if word.lower() in SentenceSimilarity.stops:
				continue
			else:
				vec = vec + model[word.lower()]
				wordCount = wordCount + 1
		return vec/wordCount
	@staticmethod
	def ComputeSentenceSimilarityScoreWithWordToVec(sentence1, sentence2):
		wordsList1 = nltk.tokenize.word_tokenize(sentence1)
		wordsList2 = nltk.tokenize.word_tokenize(sentence2)
		vec1 = SentenceSimilarity.GetVector(wordsList1, SentenceSimilarity.model)
		vec2 = SentenceSimilarity.GetVector(wordsList2, SentenceSimilarity.model)
		return SentenceSimilarity.CosineSimilarity(vec1, vec2)
if __name__=="__main__":
	sentence1 = "what are you doing this Sunday"
	sentence2 = "sunday is a holiday for us"
	print(SentenceSimilarity.ComputeSentenceSimilarityScoreWithWordToVec(sentence1, sentence2))
	print(SentenceSimilarity.ComputeSentenceSimilarityScoreWithWordToVec(sentence2, sentence1))
	print(SentenceSimilarity.ComputeSentenceSimilarityScoreWithWordToVec(sentence2, sentence1))