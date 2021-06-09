from flask import url_for
from flask_testing import TestCase
from application import app, db
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update( SQLACHEMY_DATABASE_URI='sqlite:///test.db', debug=True )
        return app
    
    def setup(self):
        db.create_all()
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop_all()

class TestsHome(TestBase):
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            m.get('http://service-2:5000/animal1', text = 'Li')
            m.post('http://service-3:5000/animal2', text = 'potamus')
            response = self.client.get(url_for("index"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Lipotamus', response.data)
    
    def test_db(self):
        with requests_mock.Mocker() as m:
            test_cases = [('Li', 'potamus'), ('Do', 'phant')]
            for test in test_cases:
                m.get('http://service-2:5000/animal1', test=case[0])
                m.post('http://service-3:5000/animal2', test=case[1])
                response = self.client.get(url_for("index"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Lipotamus', response.data)
            self.assertIn(b'Dophant', response.data)