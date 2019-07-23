import WikiData
import EntityExtraction
import SentenceSimilarity
import heapq
import numpy

class FactChecker(object):
	
    @staticmethod
    def get_top_sentences(query, sentences, k = 50):
        
        scores = []
        for sentence in sentences:
            scores.append(SentenceSimilarity.SentenceSimilarity.ComputeSentenceSimilarityScoreWithWordToVec(query, sentence))
        nscores = numpy.array(scores)
        top_k_indx = heapq.nlargest(k, range(len(a)), a.take)

        results_sentences = []
        for top_index in top_k_indx:
            results_sentences.append(sentences[top_index])
        return results_sentences
    
    @staticmethod
    def find_answer(query):
        # find entities.
        entities = EntityExtraction.EntityExtraction.get_named_entities(query)
        # Get sentences
        sentences = []
        for entity in entities:
            sentences.append(WikiData.WikiData.get_sentence(entity))
        # Top sentences
        top_sentences = get_top_sentences(query, sentences)
        print(top_sentences)
        # Get results from model.