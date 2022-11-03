from flask import Flask
import json

from Team5_Act7.1.ip_location import home

def test_base_route():
    app = Flask(__name__)
    home(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello, World!'
    assert response.status_code == 200
