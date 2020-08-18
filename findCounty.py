import pandas as pd

df = pd.read_csv("New_York_State_ZIP_Codes.csv", delimiter=',')
df = df.drop(df.columns[[1, 2, 3, 5]], axis=1)

def find_county_by_zip_code(zip_code):
    counties = []
    for index, row in df.iterrows():
        if row['ZIP Code'] == int(zip_code):
            counties.append(row['County Name'])

    if len(counties) == 1:
        return counties[0]
    else:
        return "No"


print(find_county_by_zip_code(10529))