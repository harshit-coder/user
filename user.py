from flask import Flask

app = Flask(__name__)

@app.route('/user')
def all_users():
   data= request.values
   response = data
   return jsonify(response)
   
   
@app.route('/user/user_id')
def particular_user():
   data = request.values
   response = data
   return jsonify(response)

if __name__ == '__main__':
    app.run()
