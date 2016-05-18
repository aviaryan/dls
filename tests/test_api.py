from tests import DLSTestCase, unittest
import json


class TestAPI(DLSTestCase):
    def test_404_json(self):
        resp = self.app.get('/flask.json')
        self.assertEqual(resp.status_code, 404)

    def test_text_api(self):
        self.add_text('flask', 'Yohan')
        resp = self.app.get('/flask/text')
        self.assertEqual(resp.data, 'Yohan')

    def test_json(self):
        self.add_text('flask', 'Yohan')
        self.upload('flask', 100)
        page = self.app.get('/flask.json')
        obj = json.loads(page.data)
        self.assertEqual(obj['filesize'], 100)
        self.assertEqual(obj['text'], 'Yohan')


if __name__ == '__main__':
    unittest.main()
