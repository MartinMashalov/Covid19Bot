from flask import Flask, request
from twilio.rest import Client
from test1 import send_message
import time
import findCounty as fc
from nearestCentersDictionary import nearest_centers
from makeMessage import formulate_message
from makeMessage import formulate_message_vaccine
from test import cases_data
import os, ssl
import random
from puns import puns
from vaccine_centers_nearest import refined_vaccine_sites
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


#auth_token = AccessToken('AC0d79e56293d4494c36eee4f48a59ff8e', 'SKeb5a25313bb48bd91b84eedbe6834520', 'bsamiAWrhwdHLCYpPNiy6Ch2t9WT1gAT', identity='PythonCovidBot')

auth_token = "b9d35010dbcc4e8747238c8a7fa64222"
app = Flask(__name__)
account_sid = 'AC0d79e56293d4494c36eee4f48a59ff8e'
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
bye_statements = ["bye", 'leave', 'exit', 'quit', 'goodbye']

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    print(msg)
    phone_no = request.form.get('From')
    responded = False

    if msg.lower() == "Hi".lower() or msg.lower() == "hello".lower():
        send_message("Hi There! I'm CovidBot. I'm here to help you navigate your way through this pandemic safely.", bot_number, phone_no)
        time.sleep(0.8)
        #responded = send_menu(bot_number, phone_no)
        #time.sleep(0.9)
        send_message("Your zip code is needed for some of the main features. Please supply your zip code: ", bot_number, phone_no)

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
                #county = fc.find_county_by_zip_code(zip)
                data = cases_data(county[1])
                send_message("Data for {} county:\n"
                             ""
                             "There are {} confirmed cases\n"
                             "{} deaths in total\n"
                             "{} have recovered from Covid-19\n"
                             "The number of active cases is at {}\n"
                             ""
                             "The incidence rate (number of new cases) is {}\n"
                             ""
                             "The mortality rate lies at {}.".format(data[-1], data[0], data[1], data[2], data[3], round(data[4], 2), str(round(data[5], 2)) + "%"), bot_number, phone_no)
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
        send_message("Got it!", bot_number, phone_no)
        time.sleep(0.8)
        responded = send_menu(bot_number, phone_no)

    #myths debunked (OPERATIONAL)
    elif msg.lower() == 'B'.lower():
        sent = random.choice(myths)
        send_message(sent, bot_number, phone_no)

    #nearest test centers
    elif msg.lower() == 'C'.lower():
        if phone_no in user_zips.keys():
            search = str(user_zips[phone_no][0]) + ", New York"
            centers = nearest_centers[search]

            first_test_center = formulate_message(centers[0][1])
            second_test_center = formulate_message(centers[1][1])
            third_test_center = formulate_message(centers[2][1])
            fourth_test_center = formulate_message(centers[3][1])
            fifth_test_center = formulate_message(centers[4][1])

            #print(first_test_center, fourth_test_center)
            send_message(first_test_center + "\n" + " " + "\n" + second_test_center + "\n" + " " + "\n" + third_test_center + "\n" + " " + "\n" + fourth_test_center + "\n" + " " + "\n" + fifth_test_center, bot_number, phone_no)
            '''
            send_message(formulate_message(centers[1][1]), bot_number, phone_no)
            time.sleep(1)
            send_message(formulate_message(centers[2][1]), bot_number, phone_no)
            time.sleep(1)
            send_message(formulate_message(centers[3][1]), bot_number, phone_no)'''
        else:
            send_message("Please provide a zip code and re-enter the letter you typed:  ", bot_number, phone_no)

    elif msg.lower() == 'D'.lower():
        send_message("Type the number of the friend you want to share with: ", bot_number, phone_no)

    elif msg.lower() == 'E'.lower():
        send_message("Your help is needed!", bot_number, phone_no)
        time.sleep(0.5)
        send_message("https://www.unicefusa.org/?form=HealthEmergency&utm_content=corona3responsive_E2001&ms=cpc_dig_2020_Emergencies_20200402_google_corona3responsive_delve_E2001&initialms=cpc_dig_2020_Emergencies_20200402_google_corona3responsive_delve_E2001&gclid=CjwKCAjwm_P5BRAhEiwAwRzSOyezPDpOahj2yFSuxeaXR9PKRUTNn9vkwjfOJIznTwkXF-0-HuJuFBoCdzkQAvD_BwE", bot_number, phone_no)

    elif msg.lower() == 'F'.lower():
        send_message("Covid-19 Cases: https://coronavirus.jhu.edu/map.html", bot_number, phone_no)
        time.sleep(1)
        send_message("Covid-19 Updates: https://www.nytimes.com/news-event/coronavirus?name=styln-coronavirus&region=TOP_BANNER&variant=1_Show&block=storyline_menu_recirc&action=click&pgtype=Article&impression_id=b0067c50-e244-11ea-8a15-e95204810ae6", bot_number, phone_no)

    elif len(list(msg)) == 10 or len(list(msg)) == 11 or len(list(msg)) == 12:
        if len(list(msg)) == 10:
            number = "+1" + str(msg)
            send_message("Hi There, I am CovidBot! I am a chatbot that helps guide you through the pandemic with truthful and insightful info.\n"
                         "Your friend, whose number is {} share me with you.".format(number), bot_number, number)

        elif len(list(msg)) == 11:
            number = "+" + str(msg)
            send_message(
                "Hi There, I am CovidBot! I am a chatbot that helps guide you through the pandemic with truthful and insightful info.\n"
                "Your friend, whose number is {} share me with you.".format(number), bot_number, number)

        elif len(list(msg)) == 12:
            print(msg)
            send_message(
                "Hi There, I am CovidBot! I am a chatbot that helps guide you through the pandemic with truthful and insightful info.\n"
                "Your friend, whose number is {}, shared me with you. Say Hi to activate".format(msg), bot_number, msg)

        else:
            send_message("Check if you formatted the number correct. There seems to be a mistake.", bot_number, phone_no)

    elif msg == "Puns123**":
        pun = random.choice(puns)
        send_message(pun["pun"], bot_number, phone_no)
        time.sleep(2)
        send_message(pun["punchline"], bot_number, phone_no)

    elif msg.lower() in bye_statements:
        send_message("Goodbye", bot_number, phone_no)


    #vaccine centers option addition
    elif msg.lower() == 'V'.lower():
        if phone_no in user_zips.keys():
            search = str(user_zips[phone_no][0])

            if search not in refined_vaccine_sites:
                send_message("Please provide a zip code and re-enter the letter you typed:  ", bot_number, phone_no)
            else:
                print(search)
                centers = refined_vaccine_sites[search]
                print(centers)


                first_test_center = formulate_message_vaccine(centers[0][1])
                second_test_center = formulate_message_vaccine(centers[1][1])
                third_test_center = formulate_message_vaccine(centers[2][1])
                #fourth_test_center = formulate_message_vaccine(centers[3][1])
                #fifth_test_center = formulate_message_vaccine(centers[4][1])


                send_message(
                    first_test_center + "\n" + " " + "\n" + second_test_center + "\n" + " " + "\n" + third_test_center,
                    bot_number, phone_no)

        else:
            send_message("Please provide a zip code and re-enter the letter you typed:  ", bot_number, phone_no)

    else:
        send_message("I don't understand. Here is the menu again: ", bot_number, phone_no)
        responded = send_menu(bot_number, phone_no)

    return "ok"

def send_menu(bot_num, phone_no):
    keyword = "Menu: \n" \
              "Type 'A' ->  Get Info on Cases\n" \
              "Type 'B' ->  Debunk those myths!\n" \
              "Type 'C' ->  Finds your nearest test sites\n" \
              "Type 'D' ->  Share this bot!\n" \
              "Type 'E' ->  Donate for Covid-19\n" \
              "Type 'F' ->  More Information about the virus\n" \
              "Type 'V' ->  Find your nearest vaccination site!"

    send_message(keyword, bot_num, phone_no)
    return True

if __name__ == "__main__":
    app.run(debug=True)
