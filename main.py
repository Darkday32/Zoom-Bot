import datetime
from selenium import webdriver;
import schedule
import time

driver = webdriver.Chrome('/Users/ndavi/Documents/chromedriver')
e = datetime.datetime.now()
day = (e.strftime("%a"))

# Class Times * Links

firstClass = ("05:22")
secondClass = ("13:08")
thirdClass = ("16:10")

# Links
Morning = ("https://us04web.zoom.us/j/7614926228?pwd=QW5vTDh3Q2g4eE1wMzlCY1ZycnBFUT09")
Noon = ("https://us02web.zoom.us/j/84064598955?pwd=ZGFqNXdEbkM0bUJZTjk5SUFPSElXZz09")
Evening = ("https://us02web.zoom.us/j/85718176980?pwd=aGJiZEUwb293WjFTMHN0Rk5icVZmUT09")


def monday():
    schedule.every().monday.at(firstClass).do(joinMorning)
    schedule.every().monday.at(secondClass).do(joinNoon)
    schedule.every().monday.at(thirdClass).do(joinEvening)
def tuesday():
    schedule.every().tuesday.at(firstClass).do(joinMorning)
    schedule.every().tuesday.at(secondClass).do(joinNoon)
    schedule.every().tuesday.at(thirdClass).do(joinEvening)
def wednesday():
    schedule.every().wednesday.at(firstClass).do(joinMorning)
    schedule.every().wednesday.at(secondClass).do(joinNoon)
    schedule.every().wednesday.at(thirdClass).do(joinEvening)
def thursday():
    schedule.every().thursday.at(firstClass).do(joinMorning)
    schedule.every().thursday.at(secondClass).do(joinNoon)
    schedule.every().thursday.at(thirdClass).do(joinEvening)
def friday():
    schedule.every().friday.at(firstClass).do(joinMorning)
    schedule.every().friday.at(secondClass).do(joinNoon)
    schedule.every().friday.at(thirdClass).do(joinEvening)


def joinMorning():
    driver.get(Morning)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(3600)
    driver.quit()

def joinNoon():
    driver.get(Noon)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(3600)
    driver.quit()

def joinEvening():
    driver.get(Evening)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(3600)
    driver.quit()


if day == "Mon":
     monday()
elif day == "Tue":
    tuesday()
elif day == "Wed":
     schedule.every().wednesday.at(firstClass).do(joinMorning)
elif day == "Thur":
    thursday()
elif day == "Fri":
    friday()
else:
    print("Weekend bro")


while True:
    schedule.run_pending()
    time.sleep(60)#seconds

