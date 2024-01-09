
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template, post

from final_project import *

@route('/')
def hello_world():
    return 'Hello from Bottle!'

