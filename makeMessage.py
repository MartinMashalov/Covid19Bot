from TestingCenters import full_centers_json
import json

array = []

def formulate_message(center):
    for dict in full_centers_json:
        if dict['name'] == center:
            array.append(center)
            array.append(dict['physical_address'][0]['city'])
            array.append(dict['physical_address'][0]['postal_code'])
            array.append(dict['physical_address'][0]['country'])
            array.append(dict['physical_address'][0]['state_province'])
            array.append(dict['phones'][0]['number'])

    message = "Test center in {}. \n Simply copy-paste this full address into Google Maps: " \
                  "{}, {}. \n "\
                  "Here is the center's phone number if you need to make an appointment: {}.\n" \
              "I recommend you call to make sure!".format(array[1], array[0], array[3], array[5])

    array.clear()
    return message

data_storage = None

def formulate_message_vaccine(center_search):
    with open('vaccine_centersJsonFinal.json ') as vaccine_file:
        vaccine_centers_json = json.load(vaccine_file)

        for center in vaccine_centers_json:
            address = center['address']

            if address == center_search:
                id = center['id']

        message = "Test center found!. \n Simply click on this address to go to Google Maps: " \
                  "{}. \n " \
                  "Here is the vaccine center's phone number to call: {}.\n" \
                  "Here are the vaccines available.\n Pfizer: {}, \n Moderna: {}, \n Johnson & Johnson: {} \n" \
                  "The hours are as follows. {}\n" \
                  "I recommend you call to make sure first!".format(vaccine_centers_json[id-1]['address'],
                                                              vaccine_centers_json[id-1]['contact']['phone'],
                                                              vaccine_centers_json[id-1]['vaccineBrands']['Pfizer'],
                                                              vaccine_centers_json[id-1]['vaccineBrands']['Moderna'],
                                                              vaccine_centers_json[id-1]['vaccineBrands']['Johnson & Johnson'],
                                                              vaccine_centers_json[id-1]['hours'])
    print(message)
    return message

