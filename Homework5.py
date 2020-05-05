#Danielle DiLoreto
#Homework5
#Graphs for market share of different internet browers

import matplotlib.pyplot as plt
import csv
from datetime import datetime
import numpy as np
import statistics
import pandas as pd

BROWSERS = ['Chrome', 'Firefox', 'Edge Legacy', 'IE', 'Opera']


def data_select():
  regions = {'eu' : 'browser-eu-daily.csv', 'us' : 'browser-us-daily.csv', 'as' : 'browser-as-daily.csv'}
  select = ''
  while select not in regions:
      select = input("Enter 'eu' for Europe, 'us' for United States, or 'as' for Asia: ").lower()
      if select in regions:
          break
      print('Invalid input')

  rightFile = regions[select]
  return rightFile, select.upper()


def read_data(filename):
    browser_data ={}
    data = open(filename, 'r')
    read1 = pd.read_csv(data) #stack overflow
    # grab the column data from pandas df, convert it to a list
    datesOld = read1['Date'].values.tolist() #https://thispointer.com/pandas-convert-a-dataframe-column-into-a-list-using-series-to_list-or-numpy-ndarray-tolist-in-python/
    dates = []
    for date in datesOld:
        newDate = datetime.strptime(date, "%Y-%m-%d")
        dates.append(newDate)
    chrome = read1['Chrome'].values.tolist()
    firefox = read1['Firefox'].values.tolist()
    edge = read1['Edge Legacy'].values.tolist()
    ie = read1['IE'].values.tolist()
    opera = read1['Opera'].values.tolist()

    # add each list as a key:value pair to the browser_data dict
    browser_data['dates'] = dates
    browser_data['Chrome'] = chrome
    browser_data['Firefox'] = firefox
    browser_data['Edge_Legacy'] = edge
    browser_data['Internet_Explorer'] = ie
    browser_data['Opera'] = opera

    return browser_data


def line_chart(browser_data, region):
    dates = browser_data['dates']
    y1 = browser_data['Chrome']
    y2 = browser_data['Firefox']
    y3 = browser_data['Edge_Legacy']
    y4 = browser_data['Internet_Explorer']
    y5 = browser_data['Opera']

    fig, ax = plt.subplots()
    ax.plot(dates, y1)
    ax.plot(dates, y2)
    ax.plot(dates, y3)
    ax.plot(dates, y4)
    ax.plot(dates, y5)


    ax.set(xlabel='Year', ylabel='Usage', title=('Browser Usage-' + region))
    plt.xticks(rotation=45) #https://kite.com/python/answers/how-to-rotate-axis-labels-in-matplotlib-in-python
    ax.grid()
    ax.legend(BROWSERS)
    plt.show()

def pie(browser_data, region):
   day1 =[]
   chromeDay = browser_data['Chrome'][0]
   fireDay = browser_data['Firefox'][0]
   ELDay = browser_data['Edge_Legacy'][0]
   IEDay = browser_data['Internet_Explorer'][0]
   operaDay = browser_data['Opera'][0]
   day1.append(chromeDay)
   day1.append(fireDay)
   day1.append(ELDay)
   day1.append(IEDay)
   day1.append(operaDay)


   #plot
   fig,ax = plt.subplots()
   ax.set_title("Browser Usage-" + region)
   ax.axis('equal')
   regions = BROWSERS
   values = day1
   ax.pie(values, labels = regions,explode=(0.13, 0, 0, 0, 0),autopct='%1.2f%%')
   plt.show()

def bar_chart(browser_data, region):
   avgAll = []
   avgChrome = sum(browser_data['Chrome']) / len(browser_data['Chrome'])
   avgFirefox = sum(browser_data['Firefox']) / len(browser_data['Firefox'])
   avgEdge = sum(browser_data['Edge_Legacy']) / len(browser_data['Edge_Legacy'])
   avgIE = sum(browser_data['Internet_Explorer']) / len(browser_data['Internet_Explorer'])
   avgOpera = sum(browser_data['Opera']) / len(browser_data['Opera'])
   avgAll.append(avgChrome)
   avgAll.append(avgFirefox)
   avgAll.append(avgEdge)
   avgAll.append(avgIE)
   avgAll.append(avgOpera)

   #plot
   fig, axes = plt.subplots()
   browers = BROWSERS
   values = avgAll
   axes.set_title('Browser Usage-' + region)
   axes.bar(browers,values, color=['magenta', 'red', 'green', 'blue', 'cyan'])
   axes.set_ylabel("Browser Usage")
   axes.set_xlabel("Browsers")
   plt.show()
   print('Average Market Share: ')
   i=0
   for value in avgAll:
       print(f"{BROWSERS[i]}:{value:5.2f}")
       i+=1

def main():
    fname, region = data_select()
    browser_data = read_data(fname)
    line_chart(browser_data, region)
    pie(browser_data, region)
    bar_chart(browser_data, region)
    #print(browser_data)


main()
