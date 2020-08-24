import schedule
import time
import urllib.request
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def download():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-15-2020.csv"
    filename, headers = urllib.request.urlretrieve(url, filename="/Users/martinmashalov/Documents/Python/twilioTest2/CovidData.csv")

#test function to test out schedule
def printTest():
    print("this is from the test print func")
#########################################

schedule.every(1).day.do(download)
while True:
    schedule.run_pending()
    time.sleep(1)

