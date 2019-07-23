import WikiApi
import EntityExtraction
import SentenceSimilarity
import heapq
import numpy
import DLFactory
import sys

class FactChecker(object):
	
    @staticmethod
    def get_top_sentences(query, sentences, k = 50):
        
        scores = []
        for sentence in sentences:
            scores.append(SentenceSimilarity.SentenceSimilarity.ComputeSentenceSimilarityScoreWithWordToVec(query, sentence))
        nscores = numpy.array(scores)
        top_k_indx = heapq.nlargest(k, range(len(nscores)), nscores.take)

        results_sentences = []
        for top_index in top_k_indx:
            results_sentences.append(sentences[top_index])

        # TODO add sentences which contains entities.
        return results_sentences
    
    @staticmethod
    def find_answer(query):
        # find entities.
        print("=========== Finding entities ============")
        entities = EntityExtraction.EntityExtraction.get_named_entities(query)
        print(entities)
        # Get sentences
        print("=========== Finding sentences ============")
        sentences = []
        for entity in entities:
            sentences.extend(WikiApi.WikiApi.get_sentence(entity))
        print(sentences)
        # Top sentences
        print("=========== Finding top sentences ============")
        top_sentences = FactChecker.get_top_sentences(query, sentences)
        print(top_sentences)
        # Get results from model.
        paragraph = ".".join(top_sentences)
        print("paragraph:: " + paragraph)
        print("=========== Finding answer ============")
        answer = DLFactory.DLFactory.predict_answer(query, paragraph)
        print(answer)
        return answer
if __name__ == "__main__":
	FactChecker.find_answer(sys.argv[1])
	for line in sys.stdin:
		if line == "exit":
				break
		FactChecker.find_answer(line)