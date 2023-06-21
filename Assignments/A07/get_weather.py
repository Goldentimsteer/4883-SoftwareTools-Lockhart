"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time       
import os                                      # needed for the sleep function
import Gui
from Gui import buildWeatherURL
from bs4 import BeautifulSoup                           # used to parse the HTML
from selenium import webdriver                          # used to render the web page
from seleniumwire import webdriver                      
from selenium.webdriver.chrome.service import Service   # Service is only needed for ChromeDriverManager
from tables import build_display



import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately




def asyncGetWeather(url):
        """Returns the page source HTML from a URL rendered by ChromeDriver.
        Args:
            url (str): The URL to get the page source HTML from.
        Returns:
            str: The page source HTML from the URL.
            
        Help:
        https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
        """
        
        #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
        service = Service(executable_path='/usr/local/bin/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        
        driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 5 seconds for dynamic data to load...") # changed to 5 seconds to insure the page is fully loaded 
        time.sleep(5)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML
    
if __name__=='__main__':

    url = buildWeatherURL()
    # get the page source HTML from the URL

    page = asyncGetWeather(url)

    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
     
    # find the appropriate tag that contains the weather data
    history = soup.find('lib-city-history-observation')
    soup.contents
    table = history.findAll("table")
    # print the parsed HTML
    table1 = table[0]

    #if statement since daily info is diffrent from month and weekly
    if 'daily' in url:
        lists = []
        for row in table1.findAll("tr"):
            tempList = []
            for item in row.findAll("td"):
                 tempList.append(item.text)
            if len(tempList) > 0:
                lists.append(tempList)
               
        build_display(lists, True)
        
    else:
        #Since the weekly and Monthly had the information arranged the same,  
        #so they where both sorted so the data would appear the right way on
        #on the Window display.
        lists = []
        count = 0
        for row in table1.findAll("tr"):
            if count > 1:
                tempList = []
                for item in row.findAll("td"):
                    tempList.append(item.text)
                lists.append(tempList)
            count += 1

        table = []
        tempTable = []
        i = 0
        for data in lists:
            if 'Max' in data[0] or 'Total' in data[0]:
                table.append(tempTable)
                tempTable = []
                fullText = ""
                for text in data:
                    fullText += text + " "
                tempTable.append(fullText.strip())
            else:
                fullText = ""
                for text in data:
                    fullText += text + " "
                tempTable.append(fullText.strip())
        table.append(tempTable)
        build_display(table, False)
