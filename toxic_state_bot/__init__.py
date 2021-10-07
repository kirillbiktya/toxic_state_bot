import flask

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    print(flask.request.json)
    return 'ok', 200
