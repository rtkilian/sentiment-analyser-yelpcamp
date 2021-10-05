from flask import Flask, render_template

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

app = Flask(__name__)


@app.route('/')
def process_sentiment():
    text = 'This campsite was okay'
    doc = nlp(text)
    score = doc._.polarity
    return render_template('index.html', score=score)


if __name__ == '__main__':
    app.run(debug=True)
