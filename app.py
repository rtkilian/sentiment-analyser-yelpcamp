import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
text = 'I had a really great day. It was the best day ever! But every now and then I have a really good day that makes me happy.'
doc = nlp(text)

print(doc._.polarity)
