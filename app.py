from flask import Flask

app = Flask(__name__)

from main_blueprint import main
app.register_blueprint(main)


@app.route('/')
def index():
    return 'Hello, world!'

