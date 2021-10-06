from flask import Flask, request

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def process_sentiment():
    if request.method == 'POST':
        review = request.form['review']
        doc = nlp(review)
        score = doc._.polarity
        return {'score': score}


if __name__ == '__main__':
    app.run(debug=True)
