from flask import Flask, request
from twilio.rest import Client
from test1 import send_message
import time
import findCounty as fc
from nearestCentersDictionary import nearest_centers
from test import formulate_message
import urllib.request
import os, ssl
import random
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context



app = Flask(__name__)
account_sid = 'AC0d79e56293d4494c36eee4f48a59ff8e'
auth_token = '0564dd82c87dedf2c130e8db7f5244a8'
client = Client(account_sid, auth_token)
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
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    responded = False

    if msg.lower() == "Hi".lower() or msg.lower() == "hello".lower():
        send_message("Hi There! I'm CovidBot. I'm here to help you navigate your way through this pandemic safely.", bot_number, phone_no)
        time.sleep(1)
        responded = send_menu(bot_number, phone_no)

    elif msg.lower() == "joke".lower():
        send_message("Hippos are blue?", bot_number, phone_no)

    #latest numbers
    elif msg == 'A':
        if phone_no in user_zips.keys():
            zip = user_zips[phone_no][0]
            county = fc.find_county_by_zip_code(zip)
            if county[1] == "No":
               send_message("Enter a valid zip code. Otherwise, I'm sorry, I cannot retrieve data for you :(", bot_number, phone_no)
            elif county[0] == 2:
                send_message("Which county are you located in: {}".format(county[1]), bot_number, phone_no)
            # length 1, no need for more user input
            else:
                send_message("The number of cases are: (Westchester not complete)  ", bot_number, phone_no)
        else:
            send_message("Supply a zip code:", bot_number, phone_no)

    #store zip_code (OPERATIONAL)
    elif len(list(msg)) == 5:
        #make sure there are no duplicates or if the first time, there is an incorrect value, get rid of it to store new value
        print(user_zips)
        if phone_no not in user_zips.keys():
            user_zips[phone_no] = [int(msg)]
        else:
            del user_zips[phone_no]
            user_zips[phone_no] = [int(msg)]
        send_message("Got it! Re-enter the letter you type before.", bot_number, phone_no)
        print(user_zips)

    #myths debunked (OPERATIONAL)
    elif msg.lower() == 'B'.lower():
        sent = random.choice(myths)
        send_message(sent, bot_number, phone_no)

    #nearest test centers
    elif msg.lower() == 'C'.lower():
        if phone_no in user_zips.keys():
            search = str(user_zips[phone_no][0]) + ", New York"
            centers = nearest_centers[search]

            print(centers)

            send_message(formulate_message(centers[0][1]), bot_number, phone_no)
            time.sleep(1)
            '''
            send_message(formulate_message(centers[1][1]), bot_number, phone_no)
            time.sleep(1)
            send_message(formulate_message(centers[2][1]), bot_number, phone_no)
            time.sleep(1)
            send_message(formulate_message(centers[3][1]), bot_number, phone_no)'''
        else:
            send_message("Please provide a zip code and re-enter the letter you typed:  ", bot_number, phone_no)

    else:
        send_message("I don't understand. Here is the menu again: ", bot_number, phone_no)
        responded = send_menu(bot_number, phone_no)

    return "ok"

'''
def download_csv():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-15-2020.csv"
    print("download start!")
    filename, headers = urllib.request.urlretrieve(url, filename="/Users/martinmashalov/Documents/Python/twilioTest2/CovidData.csv")
    print("download complete!")
    print("download file location: ", filename)'''

def send_menu(bot_num, phone_no):
    keyword = "Type 'A' ->  Get Info on Cases\n" \
              "Type 'B' ->  Debunk those myths!\n" \
              "Type 'C' ->  Finds the nearest Covid-19 testing centers"
    send_message(keyword, bot_num, phone_no)
    return True

if __name__ == "__main__":
    app.run(debug=True)