from tests import DLSTestCase, unittest


class TestInterface(DLSTestCase):
    def test_empty_url(self):
        page = self.app.get('/flask/')
        self.assertTrue('Nothing here' in page.data)

    def test_no_trailing_slash_redirect(self):
        page = self.app.get('/flask')
        self.assertEqual(301, page.status_code)

    def test_add_text(self):
        page = self.add_text('flask', 'luffy')
        self.assertFalse('Nothing here' in page.data)
        self.assertTrue('luffy' in page.data)

    def test_update_text(self):
        page = self.add_text('flask', 'luffy')
        self.assertTrue('luffy' in page.data)
        page = self.add_text('flask', 'zoro')
        self.assertTrue('zoro' in page.data)


if __name__ == '__main__':
    unittest.main()
