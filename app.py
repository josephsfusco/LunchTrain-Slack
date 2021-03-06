from flask import Flask, request, Response
import Train
import json
import kookify

app = Flask(__name__)
station = Train.Station()

@app.route("/", methods=['POST'])
def TrainStation():
    #TODO: Set auth to check request is coming from slack
    token = request.form.get('token')
    message = request.form.get('text')
    user_name = request.form.get('user_name')
    user_id = request.form.get('user_id')


    data = kookify.Handler(token, message, user_name, user_id)
    
#    data = {
#        "text": "hello world",
#        "text": Train.Handler(station, user_name, message),
#        "response_type": 'in_channel'
#    }

    return Response(response=json.dumps(data), status=200, mimetype="application/json")


#@app.route("/test", methods=['GET'])
@app.route('/test')
def HelloWorld():
    print("hellow world")
    return "Everything OK!"


if __name__ == '__main__':
    print("hello!")
    app.run(debug=True)

