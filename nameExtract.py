import re
import spacy
nlp=spacy.load("en_core_web_md")


def extract_names(document):
    names = []
   
    document=nlp(document)
    for tokens in document:
        s=str(tokens)
        s=re.sub("^[a-z]",s[0].upper(),s)
        t=nlp(s)
        token=t[0]
        if(token.text.lower() != "name"):
            if(token.tag_.lower() == "jj" or token.tag_.lower() == "nnp" or token.tag_.lower() == "nn" or token.tag_.lower() == "uh" or token.pos_.lower() == "noun"):
                names.append(token.text)
                break
    return names