import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
closest_distance_dict = {}


zip_codes = ["10522, New York", "10533, New York", "10530, New York", "10502, New York", "10706, New York", '10607, New York', '10710, New York', '10701, New York', '10703, New York', '10708, New York', '10709, New York']

nearest_centers_zip_codes = {}


def driving_distance(add1, add2):
    PATH = "/Users/martinmashalov/Documents/chromedriver 2"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.mapdevelopers.com/distance_from_to.php")

    address1 = driver.find_element_by_id("fromInput")
    address2 = driver.find_element_by_id("toInput")

    address1.send_keys(add1)


    for address in add2:
        address2.clear()
        address2.send_keys(address)

        button = driver.find_element_by_class_name("link_button").click()
        time.sleep(5)

        driving_distance = driver.find_element_by_id("driving_status")
        driving_distance_text = driving_distance.text
        closest_distance_dict[address] = driving_distance_text

    driver.quit()
    return closest_distance_dict

def process_distance(add1, add2):
    for add in add1:
        nearest_center_tuples = []
        closest_distance_dict = driving_distance(add, add2)
        for location, value in closest_distance_dict.items():
            miles = float(''.join(list(value)[18:22]))
            nearest_center_tuples.append((miles, location))
        nearest_center_tuples.sort()
        nearest_centers_zip_codes[add] = nearest_center_tuples[0:5]

    return nearest_centers_zip_codes

add2 = ['Stony Brook University, NY', 'Dutchess Stadium, 1500 NY-9D', '300 Enterprise Drive, NY, 12401', '462 1st Avenue, New York, NY 10016', '79-01 Broadway, New York', '506 Lenox Avenue, New York, NY', '1901 1st Avenue, New York, NY 10029', '451 Clarkson Avenue, Brooklyn, NY', '234 East 149th Street, Bronx, NY', '760 Broadway, Brooklyn, NY', '82-68 164th Street, Jamaica, NY', '2601 Ocean Parkway, Brooklyn, NY', '1400 Pelham Parkway South, Bronx, NY', '1225 Gerard Avenue, Bronx, NY', '545 East 142nd Street, Bronx, NY', '100 North Portland Avenue, Brooklyn, NY', '2094 Pitkin Avenue, Brooklyn, NY', '227 Madison Street, New York, NY', '264 West 118th Street, New York, NY', '165 Vanderbilt Avenue, Staten Island, NY', 'Palisades Parkway, NY', 'Weyman Ave, New Rochelle, NY', '1 Ocean Pkwy, New York', '555 N. Broadway, New York', '3 Delaware Drive, Lake Success, NY', '10033 4th Ave. Brooklyn, NY', '291 3rd Ave. New York', '254-61 Nassau Blvd. Queens, NY', '1149 Old Country Road, Riverhead, NY', '1167 Wantagh Ave. Wantagh, NY', '1601 3rd Ave. New York', '147 Lake St, Newburgh, NY', '1400 Pelham Parkway South Bronx, New York 10461', '545 East 142nd Street Bronx, New York 10454', '30 Hamilton St, Dobbs Ferry, NY 10522', '2393 Central Park Ave, Yonkers, NY 10710', '2290 Central Park Ave, Yonkers, NY 10710', '555 S Broadway, Tarrytown, NY 10591', '650 White Plains Rd, Tarrytown, NY 10591', '155 White Plains Rd, Tarrytown, New York', '269A Livingston St, Northvale, NJ 07647', '305 N Central Ave, Hartsdale, NY 10530', '359 N Central Ave, Hartsdale, NY 10530', '2 Park Ave, Yonkers, NY 10703', '259 Heathcote Rd, Scarsdale, NY 10583', '41 E Post Rd, White Plains, NY 10601', '222 Mamaroneck Ave, White Plains, NY 10605', '280 Mamaroneck Ave, White Plains, NY 10605', '7-11 S Broadway, White Plains, NY 10601', '100 Woods Rd, Valhalla, New York', '77 Quaker Ridge Rd Ste 4, New Rochelle, NY', '203 Gramatan Ave, Mt Vernon, NY', '500 Westchester Ave, West Harrison, NY 10604']
print(process_distance(zip_codes[0:2], add2))
#['Stony Brook University, NY', 'Dutchess Stadium, 1500 NY-9D', '300 Enterprise Drive', '462 First Avenue, New York, NY', '79-01 Broadway, New York', '506 Lenox Avenue, New York, NY', '1901 First Avenue, New York, NY', '451 Clarkson Avenue, Brooklyn, NY', '234 East 149th Street, Bronx, NY', '760 Broadway, Brooklyn, NY', '82-68 164th Street, Jamaica, NY', '2601 Ocean Parkway, Brooklyn, NY', '1400 Pelham Parkway South, Bronx, NY', '1225 Gerard Avenue, Bronx, NY', '545 East 142nd Street, Bronx, NY', '100 North Portland Avenue, Brooklyn, NY', '2094 Pitkin Avenue, Brooklyn, NY', '227 Madison Street, New York, NY', '264 West 118th Street, New York, NY', '165 Vanderbilt Avenue, Staten Island, NY', 'Palisades Parkway, NY', 'Weyman Ave, New Rochelle, NY', '1 Ocean Pkwy, New York', '555 N. Broadway, New York', '3 Delaware Drive, Lake Success, NY', '10033 4th Ave. Brooklyn, NY', '291 3rd Ave. New York', '254-61 Nassau Blvd. Queens, NY', '1149 Old Country Road, Riverhead, NY', '1167 Wantagh Ave. Wantagh, NY', '1601 3rd Ave. New York', '147 Lake St, Newburgh, NY', '1400 Pelham Parkway South Bronx, New York 10461', '545 East 142nd Street Bronx, New York 10454', '30 Hamilton St, Dobbs Ferry, NY 10522', '2393 Central Park Ave, Yonkers, NY 10710', '2290 Central Park Ave, Yonkers, NY 10710', '555 S Broadway, Tarrytown, NY 10591', '650 White Plains Rd, Tarrytown, NY 10591', '155 White Plains Rd, Tarrytown, New York', '269A Livingston St, Northvale, NJ 07647', '305 N Central Ave, Hartsdale, NY 10530', '359 N Central Ave, Hartsdale, NY 10530', '2 Park Ave, Yonkers, NY 10703', '259 Heathcote Rd, Scarsdale, NY 10583', '41 E Post Rd, White Plains, NY 10601', '222 Mamaroneck Ave, White Plains, NY 10605', '280 Mamaroneck Ave, White Plains, NY 10605', '7-11 S Broadway, White Plains, NY 10601', '100 Woods Rd, Valhalla, New York', '77 Quaker Ridge Rd Ste 4, New Rochelle, NY', '203 Gramatan Ave, Mt Vernon, NY', '500 Westchester Ave, West Harrison, NY 10604']
