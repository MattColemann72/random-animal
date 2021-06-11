from flask import url_for
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://service-2:5000/animal1', text='Lion')
            mocker.get('http://service-2:5000/animal1', text='Bear')
            mocker.post('http://service-4:5000/animal3', text='LionBear')
            self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'You have created a LionBear', response.data)