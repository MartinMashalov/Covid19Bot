
# correct vaccine sites data storage
refined_vaccine_sites = {
    '10522': [(2.32, '871 Saw Mill River Rd, Ardsley, NY 10502'),
              (4.23, '1230 Nepperhan Ave Yonkers, NY 10703'),
              (4.44, '333 Saw Mill River Rd Elmsford, NY 10523'), (5.7, '196 E Hartsdale Ave Hartsdale, NY 10530'),
              (6.04, '66 Main St, Yonkers, NY 10701')],
    '10533': [(2.82, '871 Saw Mill River Rd, Ardsley, NY 10502'), (4.53, '2290 Central Park Ave Yonkers, NY 10710'),
              (4.53, '35 Valley Ave Elmsford, NY, 10523'), (5.79, '333 Saw Mill River Rd Elmsford, NY 10523'),
              (6.3, '1230 Nepperhan Ave Yonkers, NY 10703')],
    '10530': [(0.11, '196 E Hartsdale Ave Hartsdale, NY 10530'), (2.62, '44 E Post Rd, White Plains, NY 10601'),
              (2.77, '24 Mamaroneck Ave, White Plains, NY 10601'), (3.06, '325 Mamaroneck Ave, White Plains, NY 10605'),
              (3.24, '199 Brook St Scarsdale, NY 10583')],
    '10502': [(0.37, '871 Saw Mill River Rd, Ardsley, NY 10502'), (2.5, '333 Saw Mill River Rd Elmsford, NY 10523'),
              (3.61, '196 E Hartsdale Ave Hartsdale, NY 10530'), (3.9, '199 Brook St Scarsdale, NY 10583'),
              (4.24, '1230 Nepperhan Ave Yonkers, NY 10703')],
    '10706': [(2.27, '1230 Nepperhan Ave Yonkers, NY 10703'), (3.51, '871 Saw Mill River Rd, Ardsley, NY 10502'),
              (5.61, '585 Yonkers Ave, Yonkers, NY 10704'), (5.64, '333 Saw Mill River Rd Elmsford, NY 10523'),
              (5.7, '66 Main St, Yonkers, NY 10701')],
    '10607': [(1.89, '35 Valley Ave Elmsford, NY, 10523'), (1.99, '24 Mamaroneck Ave, White Plains, NY 10601'),
              (2.23, '44 E Post Rd, White Plains, NY 10601'), (2.95, '333 Saw Mill River Rd Elmsford, NY 10523'),
              (3.17, '196 E Hartsdale Ave Hartsdale, NY 10530')],
    '10710': [(0.36, '66 Main St, Yonkers, NY 10701'), (0.9, '6 Mclean Ave, Yonkers, NY 10705'),
              (2.06, '585 Yonkers Ave, Yonkers, NY 10704'), (2.08, '5700 Mosholu Ave, The Bronx, NY 10471'),
              (3.03, '1230 Nepperhan Ave Yonkers, NY 10703')],
    '10701': [(0.36, '66 Main St, Yonkers, NY 10701'), (0.9, '6 Mclean Ave, Yonkers, NY 10705'),
              (2.06, '585 Yonkers Ave, Yonkers, NY 10704'), (2.08, '5700 Mosholu Ave, The Bronx, NY 10471'),
              (3.03, '1230 Nepperhan Ave Yonkers, NY 10703')],
    '10703': [(0.36, '66 Main St, Yonkers, NY 10701'), (0.9, '6 Mclean Ave, Yonkers, NY 10705'),
              (2.06, '585 Yonkers Ave, Yonkers, NY 10704'), (2.08, '5700 Mosholu Ave, The Bronx, NY 10471'),
              (3.03, '1230 Nepperhan Ave Yonkers, NY 10703')],
    '10708': [(1.49, '24 W Grand St, Mt Vernon, NY 10552'), (1.51, '370 White Plains Rd, Eastchester, NY 10709'),
              (1.55, '375 White Plains Rd, Eastchester, NY 10709'), (2.18, '111 Vredenburgh Ave, Yonkers, NY 10704'),
              (3.84, '211 E Sandford Blvd, Mt Vernon, NY 10550')],
    '10709': [(1.19, '375 White Plains Rd, Eastchester, NY 10709'), (1.22, '199 Brook St Scarsdale, NY 10583'),
              (1.33, '370 White Plains Rd, Eastchester, NY 10709'), (4.29, '761 Main St, New Rochelle, NY 10805'),
              (4.31, '551 Main St, New Rochelle, NY 10801')]}


def find_nearest_centersandSort():
    for id, zip_code in enumerate(nearest_vaccines.keys()):
        location_arr = nearest_vaccines[zip_code]
        print(id, zip_code)
        location_arr.sort()
        location_arr = location_arr[0:5]
        refined_vaccine_sites[zip_code] = location_arr

    return refined_vaccine_sites
