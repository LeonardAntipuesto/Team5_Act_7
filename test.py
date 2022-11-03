from flask import Flask
import json

from ip_location import app

def test_ip_location():
    response = app.test_client().get('/')
    assert response.status_code == 200
