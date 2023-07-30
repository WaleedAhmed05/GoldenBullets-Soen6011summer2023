import pytest
from dotenv import load_dotenv
from os import getenv, environ
from app import app as flask_app
from extensions import db

load_dotenv('../../.env', override=True)

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()
