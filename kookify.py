import threading
import time
import requests
import json


def Handler(token, message, user_name):
    if (message == "who is koty?" or message == "who is koty"): 
        response = {
            "text" : "<@U010YCYF3SM> is KOTY",
            "user" : "U010YCYF3SM",
            "response_type" : "in_channel"
        }
    else: 
        response = {
            "text" : "hello world!",
            "response_type" : "in_channel"
        }
    return response 
