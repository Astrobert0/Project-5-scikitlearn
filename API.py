import json
import requests as rq
import base64
import getpass
import re
import time

def get_oauth_token():
    """input: Apikey and Secret (password)
    It returns a dictionary with the acces token, expiration time (in seconds), token type and scope""" 

    url = "https://api.idealista.com/oauth/token" 
    key = getpass.getpass(prompt = 'Please insert the Apikey \n')
    secretkey = getpass.getpass(prompt = 'Please insert the Secret code \n')
    rule1 = 'b\''
    rule2 = '\''
  
    code = str(base64.b64encode(bytes(key + ':' + secretkey,'utf-8'))) #with the key and secretkey we need an authorization header, what it does is sum both passwords 
                                                                        #with a ':' and applies a base64 encode, assigning that encode to a variable as a string

    auth = re.sub(rule2,'',re.sub(rule1,'', code)) #variable code has some non desired characters, applies a simple regex to remove it


    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' ,'Authorization' : 'Basic ' + auth}
    params = {'grant_type':'client_credentials'}
    content = rq.post(url,headers = headers, params=params)

    return content.json()

def search_api(token, url):  

    """Function that realizes the query and returns a dict with all the data searched based on the API filters, the property data is in the key 'elementList' """

    headers = {'Content-Type': 'Content-Type: multipart/form-data;', 'Authorization' : 'Bearer ' + token}
    content = rq.post(url, headers = headers) 
    return content.json()
