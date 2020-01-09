import os

from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson.errors import InvalidId

from backends.mongo import find_records, MongoJSONEncoder, ObjectIdConverter, valid_id, get_record_by_id

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

mongo = PyMongo(app)


@app.route('/api/v1/records', methods=["GET"])
def records():
    return jsonify(find_records(mongo))

@app.route('/api/v1/records/<objectid:record_id>', methods=["GET"])
def record(record_id):
        result = get_record_by_id(mongo, record_id)
        if len(result) == 0:
            return "", 204,
        return jsonify(result)


if __name__ == '__main__':
    debug = os.getenv("DEBUG", "false") in ("1", "true", "T")
    app.run(host='0.0.0.0', debug=debug, port=8080)
