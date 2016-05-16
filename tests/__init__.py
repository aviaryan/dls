import unittest
import os
from dls import app, db


class DLSTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.sqlite3'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        os.unlink('test.sqlite3')

    def add_text(self, url, text):
        return self.app.post('/%s/edit/' % url, data={'text': text}, follow_redirects=True)
