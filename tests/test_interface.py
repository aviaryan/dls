from tests import DLSTestCase, unittest


class TestInterfaceMain(DLSTestCase):
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

    def test_locked(self):
        page = self.add_text('cg', 'lelouch')
        self.assertTrue('Lock' in page.data)
        page = self.app.post('/cg/lock', follow_redirects=True)
        self.assertFalse('Lock' in page.data)
        page = self.add_text('cg', 'rolo')
        self.assertTrue('lelouch' in page.data)


# nosetests tests.test_interface:TestInterfaceFile
class TestInterfaceFile(DLSTestCase):
    def test_upload(self):
        page = self.upload('flask', 10)
        self.assertTrue('10' in page.data)
        page = self.app.get('/flask/file')
        self.assertEqual(len(page.data), 10)
        self.assertEqual(page.status_code, 200)

    def test_upload_large(self):
        page = self.upload('flask', 1024 * 1024 * 100)  # 100 mb
        self.assertTrue('Upload' in page.data)
        page = self.app.get('/flask/file')
        self.assertEqual(page.status_code, 404, msg=page.data)

    def test_upload_locked(self):
        self.upload('cg', 11)
        self.app.post('/cg/lock')
        page = self.upload('cg', 23)
        self.assertTrue('Upload' in page.data, msg=page.data)
        self.assertTrue('Errors' in page.data)


if __name__ == '__main__':
    unittest.main()
