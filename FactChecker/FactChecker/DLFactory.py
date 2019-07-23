import numpy as np
import torch
from allennlp import predictors

#from allennlp import predictors
class DLFactory(object):
    """description of class"""
    def __init__(self):
        self.predictor = predictors.Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")
    def predict_answer(self,question,passage):
        result = self.predictor.predict(
          passage= passage,
          question= question
        )
        answer = result['best_span_str']
        return answer
if __name__=="__main__":
	question = "Who is the father of Indira Gandhi?"
	passage = "Indira Priyadarshini Gandhi was an Indian politician, stateswoman and a central figure of the Indian National Congress. She was the first and, to date, the only female Prime Minister of India. Indira Gandhi was the daughter of Jawaharlal Nehru, the first prime minister of India. She served as Prime Minister from January 1966 to March 1977 and again from January 1980 until her assassination in October 1984, making her the second longest-serving Indian Prime Minister, after her father Gandhi served as her father's personal assistant and hostess during his tenure as Prime Minister between 1947 and 1964. She was elected President of the Indian National Congress in 1959. Upon her father's death in 1964 she was appointed as a member of the Rajya Sabha (upper house) and became a member of Lal Bahadur Shastri's cabinet as Minister of Information and Broadcasting.In the Congress Party's parliamentary leadership election held in early 1966 (upon the death of Shastri), she defeated her rival Morarji Desai to become leader, and thus succeeded Shastri as Prime Minister of India."
	dlFactory = DLFactory()
	answer = dlFactory.predict_answer(question,passage)
	print(answer)
	


