import threading
import time
import requests
import json


def Handler(token, message, user_name, user_id):
    if (message == "who is koty?" or message == "who is koty"): 
        if (user_id == "U010YCYF3SM"):
            response = {
                "text" : "you are :crown: \nhttps://media.giphy.com/media/f5XoT6Bf0Vj8RqEP5p/giphy.gif",
                "response_type" : "in_channel"
            }
        else: 
            response = {
                "text" : "<@U010YCYF3SM> is KOTY :crown: :verified:",
                "user" : "U010YCYF3SM",
                "response_type" : "in_channel"
            }
    elif (message == "hi" or message == "hello"):
        response = {
            "text" : "hi kook",
            "response_type" : "in_channel"
        }
    elif (message == "log"):
        response = {
            "text" : "message: %s \ntoken: %s \nuser name: %s \nuser id: %s" % (message, token, user_name, user_id),
            "response_type" : "in_channel"
        }
    else: 
        response = {
            "text" : "all i see is :talking::talking::talking:",
            "response_type" : "in_channel"
        }
    return response 
