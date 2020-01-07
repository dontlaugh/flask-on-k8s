import os

from flask import Flask, jsonify
from flask_pymongo import PyMongo

from backends.mongo import find_records, MongoJSONEncoder, ObjectIdConverter, valid_id, get_record_by_id

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

mongo = PyMongo(app)


@app.route('/api/v1/records', methods=["GET"])
def records():

    # TODO error handling?
    return jsonify(find_records(mongo))


@app.route('/api/v1/records/<objectid:record_id>', methods=["GET"])
def record(record_id):

    if not valid_id(record_id):
        return "bad request", 400

    result = get_record_by_id(mongo, record_id)
    if len(result) is 0:
        return "", 204,

    return jsonify(result)


if __name__ == '__main__':
    # TODO extract into env vars for config
    app.run(host='0.0.0.0', debug=True, port=8080)
