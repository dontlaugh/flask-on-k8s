import os

from flask import Flask, jsonify
from flask_pymongo import PyMongo

from backends.mongo import find_records, MongoJSONEncoder, ObjectIdConverter

# export MONGO_URI=mongodb://YOUR_USERNAME:YOUR_PASSWORD@YOUR_MONGO_HOST:YOUR_MONGO_PORT/YOUR_MONGO_DB_NAME

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

mongo = PyMongo(app)


@app.route('/api/v1/records')
def records():

    # TODO error handling?
    return jsonify(find_records(mongo))


@app.route('/api/v1/records/<record_id>')
def record(record_id):

    # TODO error handling?

    result = find_records(mongo, record_id)
    if len(result) is 0:
        return "", 204,

    return jsonify(result)


if __name__ == '__main__':
    # TODO extract into env vars for config
    app.run(host='0.0.0.0', debug=True, port=8080)
