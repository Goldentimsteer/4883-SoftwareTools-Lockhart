
import PySimpleGUI as sg  
import json
import pandas 

#set dropdown menu items
m = ["1","2","3","4","5","6","7","8","9","10","11","12"]
d = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"] 
y = ["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"]

dwm = ["daily","weekly","monthly"]


def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return.  Valid values are 'tuple', 'list', or 'dict'.
    """
    from datetime import datetime
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]

    return {
        'day':datetime.now().day,
        'month':datetime.now().month,
        'year':datetime.now().year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):
    """ A gui to pass parameters to get the weather from the web.
    Args:
        month (int): The month to get the weather for.
        day (int): The day to get the weather for.
        year (int): The year to get the weather for.
    Returns:
        Should return a URL like this, but replace the month, day, and year, filter, and airport with the values passed in.
        https://www.wunderground.com/history/daily/KCHO/date/2020-12-31
    """
    current_month,current_day,current_year = currentDate('tuple')
    
    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year

    #use panda to read in airport codes 
    c = pandas.read_json('airports-better.json')
    c = c.sort_values(by=["icao"])
    c1 = c['icao'].tolist()
    
    # Create the gui's layout using text boxes that allow for user input without checking for valid input
    layout = [
        [sg.Text('Month')],[sg.DD(m,size = (10,8) )],
        [sg.Text('Day')],[sg.DD(d,size= (10,8))],
        [sg.Text('Year')],[sg.DD(y,size = (10,8))],
        [sg.Text('Code')],[sg.DD(c1,size = (10,8))],
        [sg.Text('daily / weekly / monthly')],[sg.DD(dwm,size = (10,8))],
        [sg.Submit(), sg.Cancel()]
    ]      

    
    window = sg.Window('Get The Weather', layout)    

    event, values = window.read()
    window.close()
        
    month = values[0]
    day = values[1]
    year = values[2]
    airport = values[3]
    filter = values[4]

   
    #if no data has been inputed 
    if len(str(month)) < 1:
        month = current_month
    if len(str(day)) < 1:
        day = current_day
    if len(str(year)) < 1:
        year = current_year
    if len(airport) < 1:
        airport = "EDDB"
    if len(filter) < 1:
        filter = "monthly"
    
    base_url = "https://wunderground.com/history"

    url = f"{base_url}/{filter}/{airport}/date/{year}-{month}-{day}"
    return url

    # return the URL to pass to wunderground to get appropriate weather data

if __name__=='__main__':
    buildWeatherURL()

