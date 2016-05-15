from tests import DLSTestCase, unittest


class TestInterface(DLSTestCase):
    def test_empty_url(self):
        page = self.app.get('/flask/')
        self.assertTrue('Nothing here' in page.data, msg=page.data)

    def test_no_trailing_slash_redirect(self):
        page = self.app.get('/flask')
        self.assertEqual(301, page.status_code, msg=page)


if __name__ == '__main__':
    unittest.main()
