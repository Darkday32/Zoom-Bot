import time
from info import Evening, Morning, Noon
from main import driver

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