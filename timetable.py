import schedule
from info import firstClass, secondClass, thirdClass
from join import joinMorning, joinEvening, joinNoon
import time

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

while True:
    schedule.run_pending()
    time.sleep(60)#seconds