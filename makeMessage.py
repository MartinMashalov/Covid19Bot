from TestingCenters import full_centers_json

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
