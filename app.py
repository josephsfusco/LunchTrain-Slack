from flask import Flask, request, Response
import Train
import json

app = Flask(__name__)
station = Train.Station()


@app.route("/", methods=['POST'])
def postToSlack():

    webhook_url = "https://hooks.slack.com/services/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"
    
    slack_data = {
        'text': "hello world :crown::crown:", 
        }

    response = requests.post(webhook_url, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'})
    print(response)




#def TrainStation():
#    print("hit the train station")
#    #TODO: Set auth to check request is coming from slack
#    token = request.form.get('token')
#    message = request.form.get('text')
#    user_name = request.form.get('user_name')
#    data = {
#        "text": Train.Handler(station, user_name, message),
#        "response_type": 'in_channel'
#    }
#    return Response(response=json.dumps(data.text), status=200, mimetype="application/json#")


#@app.route("/test", methods=['GET'])
@app.route('/test')
def HelloWorld():
    print("hellow world")
    return "Everything OK!"


if __name__ == '__main__':
    print("hello!")
    app.run(debug=True)

