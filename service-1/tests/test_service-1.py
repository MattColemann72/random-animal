from flask import url_for
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from unittest.mock import patch
import requests_mock

from application import app, db


class TestBase(TestCase):
    def create_app(self):
        
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                DEBUG=True
                )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# class TestHome(TestBase):
#     def test_home(self):
#         with requests_mock.Mocker() as mocker:
#             mocker.get('http://service-2:5000/animal1', text='Lion')
#             mocker.get('http://service-3:5000/animal2', text='Bear')
#             mocker.post('http://service-4:5000/animal3', text='LionBear')
#             response = self.client.get(url_for('index'))
#             self.assertEqual(response.status_code, 200)
#             self.assertIn(b'You have created a LionBear', response.data)
    
    def test_home(self):
        with patch("random.choice") as random:
            random.return_value = "Lion"
            response = self.client.get(url_for('index'))
            self.assertIn(b'Lion', response.data)