from flask import Flask


app = Flask(__name__)

@app.route('/user')
def all_users():
   with open('./sample.json', 'r') as jsonfi:
      data = json.loads(jsonfi.read())
      return json.dumps(data)   
   
   
@app.route('/user/user_id')
def particular_user():
   user_id = request.values
   with open('./sample.json', 'r') as jsonfi:
      data = json.loads(jsonfi.read())
      return json.dumps(data[user_id])   
   
if __name__ == '__main__':
    app.run()
