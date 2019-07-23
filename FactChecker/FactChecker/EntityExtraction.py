from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import sys

class EntityExtraction(object):
	@staticmethod
	def get_named_entities(text):
		chunked = ne_chunk(pos_tag(word_tokenize(text)))
		continuous_chunk = []
		current_chunk = []
		print("get_named_entities:: text " + text)
		for i in chunked:
			if type(i) == Tree:
				current_chunk.append(" ".join([token for token, pos in i.leaves()]))
			elif current_chunk:
				named_entity = " ".join(current_chunk)
				if named_entity not in continuous_chunk:
					continuous_chunk.append(named_entity)
					current_chunk = []
			else:
				continue
		print("get_named_entities:: entities " + " ,".join(continuous_chunk))
		return continuous_chunk


if __name__ == "__main__":
    EntityExtraction.get_named_entities(sys.argv[1])