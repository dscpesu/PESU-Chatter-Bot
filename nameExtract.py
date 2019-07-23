import re
import nltk
from nltk.corpus import stopwords
import spacy
stop = stopwords.words('english')


#def ie_preprocess(document):
 #   document = ' '.join([i for i in document.split() if i not in stop])
 #   sentences = nltk.sent_tokenize(document)
  #  sentences = [nltk.word_tokenize(sent) for sent in sentences]
   # sentences = [nltk.pos_tag(sent) for sent in sentences]
    #return sentences

def extract_names(document):
    names = []
    #sentences = ie_preprocess(document)
    #for tagged_sentence in sentences:
     #   for chunk in nltk.ne_chunk(tagged_sentence):
      #      if type(chunk) == nltk.tree.Tree:
       #         if chunk.label() == 'PERSON':
        #            names.append(' '.join([c[0] for c in chunk]))
    #return names
    for token in document:
        if(token.text.lower() != "name"):
            if(token.tag_.lower() == "jj" or token.tag_.lower() == "nnp" or token.tag_.lower() == "nn" or token.tag_.lower() == "uh" or token.pos_.lower() == "noun"):
                names.append(token.text)
    return names