import isodate as iso

from datetime import date, datetime

from bson import ObjectId
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter


class MongoJSONEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, (datetime, date)):
            return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


class ObjectIdConverter(BaseConverter):

    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)


def find_records(mongo):
    return list(mongo.db.record.find({}))


def get_record_by_id(mongo, _id):
    query = {"_id": _id}
    results = mongo.db.record.find(query)
    return list(results)


def valid_id(_id):
    return ObjectId.is_valid(_id)