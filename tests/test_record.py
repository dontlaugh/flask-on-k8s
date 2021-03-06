import backends.mongo

from unittest import TestCase

from bson.objectid import ObjectId
from mock import patch


def mock_get_record_by_id(mongo, record_id=None):
    data = [
        {
            "_id": ObjectId("5df983d2970c93051e784d90"),
            "contributor": "Colette Rosati",
            "amount": "300",
            "filing_url": "https://apps-secure.phoenix.gov/CampaignFinance/Reports/PrintReport/a645d394-f6de-4f61-a9cc-d9cdc23c73d1",
            "date": "2013-03-13",
            "recipient": "Arizona Taxpayers Action Committee"
        },
        {
            "_id": ObjectId("5df983d2970c93051e784d91"),
            "contributor": "Gumecindo Ybarra",
            "amount": "550",
            "filing_url": "https://apps-secure.phoenix.gov/CampaignFinance/Reports/PrintReport/a661fff7-871c-411d-a150-7b442eadde68",
            "date": "2013-09-25",
            "recipient": "Laura Pastor 4 City Council"
        },
        {
            "_id": ObjectId("5df983d2970c93051e784d92"),
            "contributor": "Karrin Taylor",
            "amount": "200",
            "filing_url": "https://apps-secure.phoenix.gov/CampaignFinance/Reports/PrintReport/02533263-ef56-4aa8-9480-68e3705c737f",
            "date": "2019-04-26",
            "recipient": "Vania for Phoenix"
        },
    ]
    for record in data:
        if record.get('_id') == ObjectId(record_id):
            return 1, record
    return 0, None


class TestRecord(TestCase):

    @patch('backends.mongo.get_record_by_id')
    def test_get_record_returns_a_list(self, mock_record):
        mock_record.side_effect = mock_get_record_by_id
        data = backends.mongo.get_record_by_id(None, None)
        self.assertEqual(tuple, type(data))

    @patch('backends.mongo.get_record_by_id')
    def test_get_record_returns_a_list_filtering(self, mock_record):
        mock_record.side_effect = mock_get_record_by_id
        data = backends.mongo.get_record_by_id(None, '5df983d2970c93051e784d90')
        self.assertEqual(tuple, type(data))

    @patch('backends.mongo.get_record_by_id')
    def test_get_record_returns_a_unique_element_list(self, mock_record):
        mock_record.side_effect = mock_get_record_by_id
        count, data = backends.mongo.get_record_by_id(None, '5df983d2970c93051e784d90')
        self.assertEqual(count, 1)
        self.assertTrue(data.get('contributor') == 'Colette Rosati')
