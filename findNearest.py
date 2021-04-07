import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import json
closest_distance_dict = {}


zip_codes = ["10522 Dobbs Ferry", "10533, Irvington", "10530 Hartsdale", "10502 Ardsley", "10706 Hastings", '10607 Fairview', '10710 Yonkers', '10701 Yonkers', '10703 Yonkers', '10708 Bronxville', '10709 Eastchester']

nearest_centers_zip_codes = {}


def driving_distance(add1, add2):
    PATH = "/Users/martinmashalov/Downloads/VaccineDriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.mapdevelopers.com/distance_from_to.php")

    address1 = driver.find_element_by_id("fromInput")
    address2 = driver.find_element_by_id("toInput")

    address1.send_keys(add1)


    for address in add2:
        address2.clear()
        address2.send_keys(address)

        button = driver.find_element_by_class_name("link_button").click()
        time.sleep(3.9)

        driving_distance = driver.find_element_by_id("driving_status")
        driving_distance_text = driving_distance.text
        print(driving_distance_text)
        closest_distance_dict[address] = driving_distance_text

    driver.quit()
    return closest_distance_dict

def process_distance(add1, add2):
    for add in add1:
        print(add)
        nearest_center_tuples = []
        closest_distance_dict = driving_distance(add, add2)
        for location, value in closest_distance_dict.items():
            miles = float(''.join(list(value)[18:22]))
            nearest_center_tuples.append((miles, location))
            print(miles)
        nearest_center_tuples.sort()
        nearest_centers_zip_codes[add] = nearest_center_tuples[0:5]

    return nearest_centers_zip_codes

add2 = ['Stony Brook University, NY', 'Dutchess Stadium, 1500 NY-9D', '300 Enterprise Drive, NY, 12401', '462 1st Avenue, New York, NY 10016', '79-01 Broadway, New York', '506 Lenox Avenue, New York, NY', '1901 1st Avenue, New York, NY 10029', '451 Clarkson Avenue, Brooklyn, NY', '234 East 149th Street, Bronx, NY', '760 Broadway, Brooklyn, NY', '82-68 164th Street, Jamaica, NY', '2601 Ocean Parkway, Brooklyn, NY', '1400 Pelham Parkway South, Bronx, NY', '1225 Gerard Avenue, Bronx, NY', '545 East 142nd Street, Bronx, NY', '100 North Portland Avenue, Brooklyn, NY', '2094 Pitkin Avenue, Brooklyn, NY', '227 Madison Street, New York, NY', '264 West 118th Street, New York, NY', '165 Vanderbilt Avenue, Staten Island, NY', 'Palisades Parkway, NY', 'Weyman Ave, New Rochelle, NY', '1 Ocean Pkwy, New York', '555 N. Broadway, New York', '3 Delaware Drive, Lake Success, NY', '10033 4th Ave. Brooklyn, NY', '291 3rd Ave. New York', '254-61 Nassau Blvd. Queens, NY', '1149 Old Country Road, Riverhead, NY', '1167 Wantagh Ave. Wantagh, NY', '1601 3rd Ave. New York', '147 Lake St, Newburgh, NY', '1400 Pelham Parkway South Bronx, New York 10461', '545 East 142nd Street Bronx, New York 10454', '30 Hamilton St, Dobbs Ferry, NY 10522', '2393 Central Park Ave, Yonkers, NY 10710', '2290 Central Park Ave, Yonkers, NY 10710', '555 S Broadway, Tarrytown, NY 10591', '650 White Plains Rd, Tarrytown, NY 10591', '155 White Plains Rd, Tarrytown, New York', '269A Livingston St, Northvale, NJ 07647', '305 N Central Ave, Hartsdale, NY 10530', '359 N Central Ave, Hartsdale, NY 10530', '2 Park Ave, Yonkers, NY 10703', '259 Heathcote Rd, Scarsdale, NY 10583', '41 E Post Rd, White Plains, NY 10601', '222 Mamaroneck Ave, White Plains, NY 10605', '280 Mamaroneck Ave, White Plains, NY 10605', '7-11 S Broadway, White Plains, NY 10601', '100 Woods Rd, Valhalla, New York', '77 Quaker Ridge Rd Ste 4, New Rochelle, NY', '203 Gramatan Ave, Mt Vernon, NY', '500 Westchester Ave, West Harrison, NY 10604']
#print(process_distance(zip_codes, add2))
vaccine_address = ['871 Saw Mill River Rd, Ardsley, NY 10502', '35 Valley Ave Elmsford, NY, 10523', '2290 Central Park Ave Yonkers, NY 10710', '1230 Nepperhan Ave Yonkers, NY 10703', '81 Ny-303 Tappan, NY 10983', '196 E Hartsdale Ave Hartsdale, NY 10530', '269a Livingston St Northvale, NJ 07647', '333 Saw Mill River Rd Elmsford, NY 10523', '199 Brook St Scarsdale, NY 10583', '199 Brook St Scarsdale, NY 10583', '44 E Post Rd, White Plains, NY 10601', '375 White Plains Rd, Eastchester, NY 10709', '370 White Plains Rd, Eastchester, NY 10709', '24 Mamaroneck Ave, White Plains, NY 10601', '325 Mamaroneck Ave, White Plains, NY 10605', '16 Ny-59, Nyack, NY 10960', '154 Westchester Ave, White Plains, NY 10601', '670 N Broadway, White Plains, NY 10603', '66 Main St, Yonkers, NY 10701', '585 Yonkers Ave, Yonkers, NY 10704', '111 Vredenburgh Ave, Yonkers, NY 10704', '24 W Grand St, Mt Vernon, NY 10552', '6 Mclean Ave, Yonkers, NY 10705', '1046 Yonkers Ave, Yonkers, NY 10704', '5700 Mosholu Ave, The Bronx, NY 10471', '678 Mclean Ave, Yonkers, NY 10704', '2425 Palmer Ave, New Rochelle, NY 10801', '211 E Sandford Blvd, Mt Vernon, NY 10550', '50 W Madison Ave, Dumont, NJ 07628', '175 Memorial Hwy Suite 1-14, New Rochelle, NY 10801', '35 Kensico Rd, Thornwood, NY 10594', '1310 Boston Post Road Ferndale Shopping Center, Larchmont, NY 10538', '4232 Baychester Ave, The Bronx, NY 10466', '202 S Highland Ave, Ossining, NY 10562', '1333 W Boston Post Rd, Larchmont, NY 10538', '1024 Broadway, Thornwood, NY 10594', '4159 White Plains Rd, The Bronx, NY 10466', '551 Main St, New Rochelle, NY 10801', '32 S Middletown Rd, Nanuet, NY 10954', '761 Main St, New Rochelle, NY 10805', '1179 E 233rd St, The Bronx, NY 10466', '20 W Hudson Ave, Englewood, NJ 07631', '10 Portland Ave, Bergenfield, NJ 07621', '3901 White Plains Rd, The Bronx, NY 10466', '5825 Broadway, The Bronx, NY 10463', '3547 Johnson Ave, The Bronx, NY 10463', '541 W 235th St, The Bronx, NY 10463', '350 Engle St, Englewood, NJ 07631', '558 W 235th St, The Bronx, NY 10463', '3480 Jerome Ave, The Bronx, NY 10467']
#print(process_distance(zip_codes, vaccine_address))