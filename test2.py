from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from test1 import send_message
import findCounty as fc
import time
import requests
import urllib.request
import os, ssl
import random
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
account_sid = 'AC0d79e56293d4494c36eee4f48a59ff8e'
auth_token = '6120cce02a157c3a76eff6ca72d98d76'
client = Client(account_sid, auth_token)
#print(client)
bot_number = "+14155238886"

user_zips = {}

myths = [
    'Covid-19 is not waterborne; however, it is aerosolic and airborne',
    'Covid-19 is not created in a lab as conspiracy theorists would say',
    'No you cannot get a face-mask exception card. You must wear a mask to stop the infection from spreading',
    'Injecting or drinking products such as alcohol and bleach will not make you immmune to Covid-19 or cure you if you tested positive',
    'Ordering products from overseas will not make you or your family sick from Covid-19',
    'Masks absolutely help stop the disease. Be mindful when going out and meeting with others please'
]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    #print("hello from top")
    msg = request.form.get('Body')
    last_msg = msg
    phone_no = request.form.get('From')
    responded = False

    if msg.lower() == "Hi".lower() or msg.lower() == "hello".lower():
        send_message("Hello there", bot_number, phone_no)
        responded = send_menu(bot_number, phone_no)

    if msg.lower() == "joke".lower():
        send_message("Hippos are blue?", bot_number, phone_no)

    #latest numbers
    if msg == 1:
        send_message("Supply a zip code:", bot_number, phone_no)

    #process zip_code, input in user_data zip_code, county, a nearest test centers array
    if type(msg) is int and len(msg) == 5:
        county = fc.find_county_by_zip_code(int(msg))
        if county == "No":
            send_message("Enter a valid zip code. Otherwise, I'm sorry, I cannot retrieve data for you :(", bot_number, phone_no)
        else: 
            # store zip codes for user
            user_zips[phone_no] = [int(msg), county]
            #send it
            send_message("The number of cases are:   ", bot_number, phone_no)

    #myths debunked
    if msg == 3:
        sent = random.choice(myths)
        send_message(sent, bot_number, phone_no)

    if msg == 4:
        pass


    return "ok"

def download_csv():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-15-2020.csv"
    print("download start!")
    filename, headers = urllib.request.urlretrieve(url, filename="/Users/martinmashalov/Documents/Python/twilioTest2/CovidData.csv")
    print("download complete!")
    print("download file location: ", filename)

#download_csv()
#download_csv("https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports_us/08-15-2020.csv")

def send_menu(bot_num, phone_no):
    keyword = 'Joke\nTestItem'
    send_message(keyword, bot_num, phone_no)
    return True

if __name__ == "__main__":
    app.run(debug=True)