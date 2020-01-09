import os

from flask import Flask, jsonify
from flask_pymongo import PyMongo
from werkzeug.exceptions import InternalServerError

from backends.mongo import find_records, MongoJSONEncoder, ObjectIdConverter, get_record_by_id

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
        count, result = get_record_by_id(mongo, record_id)
        if count == 0:
            return "", 204,
        elif count == 1:
            return jsonify(result[0])
        else:
            # If our query returns more than 1, that seems to be unrecoverable
            raise InternalServerError


if __name__ == '__main__':
    debug = os.getenv("DEBUG", "false") in ("1", "true", "T")
    app.run(host='0.0.0.0', debug=debug, port=8080)
