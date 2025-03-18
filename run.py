from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

if '__main__' == '__main__':
    app.run()