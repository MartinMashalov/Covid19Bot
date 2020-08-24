import pandas as pd


def cases_data(c):
    df = pd.read_csv("CovidData.csv")

    df = df[df['Country_Region'] == 'US']
    county = df[df['Admin2'] == c]

    confirmed_cases = county.iloc[:, 7].item()
    deaths = county.iloc[:, 8].item()
    recovered = county.iloc[:, 9].item()
    active = county.iloc[:, 10].item()
    incidence_rate = county.iloc[:, 12].item()
    fatality_rate = county.iloc[:, 13].item()

    return confirmed_cases, deaths, recovered, active, incidence_rate, fatality_rate, c


