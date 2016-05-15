from tests import DLSTestCase, unittest


class TestAPI(DLSTestCase):
    def test_404_response(self):
        resp = self.app.get('/flask.json')
        self.assertEqual(resp.status_code, 404)

    def test_text_api(self):
        self.add_text('flask', 'Yohan')
        resp = self.app.get('/flask/text')
        self.assertEqual(resp.data, 'Yohan')


if __name__ == '__main__':
    unittest.main()
