from flask import flask

app = FLask(__name__)

@app.route('/')
def root():
    return 'Hello'