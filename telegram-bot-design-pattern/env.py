# TODO: Add docstring
# TODO: Manage missing env vars

from os import environ, path
from dotenv import load_dotenv

DOTENV_PATH = path.join(path.dirname(__file__),'..' , '.env')
load_dotenv(DOTENV_PATH)

ENV = environ
