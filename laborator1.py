#!C:\Users\stfti\AppData\Local\Programs\Python\Python37\python.exe

import cgi
import requests
import json
import datetime


dataSet = cgi.FieldStorage()

latitude = dataSet.getvalue("latitude")
longitude = dataSet.getvalue("longitude")

logs = open("logs.txt", "w+")

def getCoordinates():
    
    # if latitude > 70.0 or latitude < -70.0 or longitude < -100 or longitude > 100 :
    #     response = requests.get("http://api.open-notify.org/iss-pass.json?lat=" + latitude + "&lon=" + longitude)
    #     r = response.status_code
    #     return r
    # else:
        response = requests.get("http://api.open-notify.org/iss-pass.json?lat=" + latitude + "&lon=" + longitude)

        data = response.json()

        logs.write(response)
        logs.write("\n")

        r = data["response"][0]["risetime"] 
        last2digits = int(r) % 100
        return str(last2digits)

def getQuote():
    print("\n")
    response = requests.get("http://numbersapi.com/" + getCoordinates() + "?json")
    data = response.json()
    logs.write(data)
    logs.write("\n")
    r = data["text"]
    return r

def getTranslation():
    text = getQuote()
    response = requests.get("https://api.funtranslations.com/translate/yoda.json?text=" + text)
    data = response.json()
    logs.write(data)
    logs.write("\n")
    r = data["contents"]["translated"]
    return r




print ("Content-type:text/html\r\n\r\n")
print ("<html><body>") 
print (getTranslation())
print("</body></html>")
