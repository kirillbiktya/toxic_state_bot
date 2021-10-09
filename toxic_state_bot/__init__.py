import flask
from toxic_state_bot.vk import types

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    # b4 need to authorize request!
    request_object = types.VKUpdate.de_json(flask.request.json)
    print(request_object.u_object.liker_id)
    return 'ok', 200
