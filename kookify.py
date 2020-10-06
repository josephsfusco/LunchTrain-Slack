import threading
import time
import requests
import json


def Handler(token, message, user_name):
    if (message == "who is koty?" or message == "who is koty"): 
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
            "text" : "message: %s \ntoken: %s \nuser name: %s" % (message, token, user_name),
            "response_type" : "in_channel"
        }
    else: 
        response = {
            "text" : "all i see is :talking::talking::talking:",
            "response_type" : "in_channel"
        }
    return response 
