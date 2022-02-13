from pip._vendor import requests
from bs4 import BeautifulSoup
import csv
import schedule 
import time

def updateWeather():
    weatherURL = "https://www.weatherbug.com/weather-forecast/10-day-weather/austintown-oh-44515"
    page = requests.get(weatherURL)

    #print(page.text)       <--- Prints entire page's code

    temperaturesPage = BeautifulSoup(page.content, "html.parser")

    #scraping the information from the page 
    allDays = temperaturesPage.find_all("span", class_="dateWrap__CardDay-sc-kqdwnh-2 iBzpTh""")
    allTemperatures = temperaturesPage.find_all("div", class_="temp")
    allConditions = temperaturesPage.find_all("div", class_="day-card__summary__description")

    #Lists
    dayList = []
    conditionList = []
    temperatureList = []

    #print(allTemperatures)
    for day in allDays:
        day = day.get_text()
        dayList.append(day)

    for condition in allConditions:
        condition = condition.get_text()
        conditionList.append(condition)

    for temperature in allTemperatures:
        temperature = temperature.get_text()
        temperatureList.append(temperature)

    with open('weatherScrape.csv', 'w', newline='') as csvfile:
        fieldnames = ['days', 'temperatures', 'conditions']
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()

        for day in dayList:
            thewriter.writerow({'days':day, 'temperatures':temperature, 'conditions':condition})

schedule.every(86400).seconds.do(updateWeather)