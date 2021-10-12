from flask import Flask, request
from flask_restful import Resource, Api, reqparse

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()  # used to parse incoming requests
parser.add_argument('review', required=True,
                    help='Review cannot be blank!')


class PredictSentiment(Resource):
    def post(self):
        args = parser.parse_args()
        review = args['review']
        doc = nlp(review)
        score = doc._.polarity
        return {'score': score}


api.add_resource(PredictSentiment, '/predict')

if __name__ == '__main__':
    app.run()
