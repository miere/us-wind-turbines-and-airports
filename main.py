#!/usr/bin/env python3
import pandas as pd
import geopy.distance


def calc_distance(point_a, point_b):
    return geopy.distance.geodesic(point_a, point_b).km


# CONSTANTS
TOO_FAR_AWAY_IN_KM = 1000000

# MAIN
airports = pd.read_csv('data/us-airports.csv') #.head(1000)
turbines = pd.read_csv('data/us-wind-turbines.csv') #.head(100)

for i, turbine in turbines.iterrows():
    print(turbine['case_id'], end='')
    turbine_location = (turbine['ylat'], turbine['xlong'])

    min_distance = TOO_FAR_AWAY_IN_KM
    for j, airport in airports.iterrows():
        print('.', end='')
        airport_location = (airport['latitude_deg'], airport['longitude_deg'])
        distance = calc_distance(airport_location, turbine_location)

        if distance <= min_distance:
            min_distance = distance

    turbines.at[i, 'closest_airport_in_km'] = min_distance
    print('\n')

turbines.to_csv('data/us-wind-turbines-updated.csv', sep=',', encoding='utf-8')
print('\nFinished\n')
