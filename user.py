import json
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/user')
def all_users():
    with open('./sample.json', 'r') as jsonfi:
        data = json.loads(jsonfi.read())
        return json.dumps(data)


@app.route('/user/<user_id>')
def particular_user(user_id):
    id = user_id
    with open('./sample.json', 'r') as jsonfi:
        data = json.loads(jsonfi.read())
        for i in data:
            if i["id"] == 1:
                dt = i
        return json.dumps(dt)


if __name__ == '__main__':
    app.run()
