
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv



description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""


app = FastAPI(

    description=description,

)

db = []

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)


def getUniqueCountries():
    global db
    countries = {}

    for row in db:
        print(row)
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())

def getUniqueWhos():
    global db
    whos = {}

    for row in db:
        print(row)
        if not row[3] in whos:
            whos[row[3]] = 0
   
    return list(whos.keys())


@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/countries/")
async def countries():

    return {"countries":getUniqueCountries()}


@app.get("/whos/")
async def whos():

    return {"whos":getUniqueWhos()}

@app.get("/casesByRegion/")
async def casesByRegion(year:int = None):
    """
    will show the amount of casses by region
    parameters 
    - year
    returns
    - cases by region

    responce body example

    {
  "data": {
    "EMRO": 4912291,
    "EURO": 27179187,
    "AFRO": 1900687,
    "WPRO": 1087695,
    "AMRO": 35799646,
    "SEARO": 11973259,
    "Other": 745
    }
    }
    """
    try:
    
        cases = {}
        
        for row in db:
            if year != None and year != int(row[0][:4]):
                continue
                
            if not row[3] in cases:
                cases[row[3]] = 0
            cases[row[3]] += int(row[4])    

        return {"data":cases,"success":True,"message":"Cases by Region","size":len(cases),"year":year}
    
    except Exception as E:
         return {"error": str(E),"success": False,"params":{
              "year": year
        }}



@app.get("/max_deaths/")

def max_deaths(year:int = None):
    """
    will show the max death
    parameters 
    - year
    returns
    - max death

    responce body example

    {
  "data": {
    "EMRO": 4912291,
   
    }
    }
    """
    try:
        if year != None and year != int(row[0][:4]):
            maxdeath = max(db)

    except Exception as E:
        return {"error": str(E),"success": False,"params":{
              "year": year
         }}

@app.get("/min_death/")
def min_death(year:int = None):
    """
    will show the min death
    parameters 
    - year
    returns
    - min death

    responce body example

    {
  "data": {
    "EMRO": 49121,
   
    }
    }
    """
    try: 
        if year != None and year != int(row[0][:4]):
            mINdeath = min(db)

    except Exception as E:
        return {"error": str(E),"success": False,"params":{
              "year": year
         }}


        
    except Exception as E:
        return {"error": str(E),"success": False,"params":{
              "year": year
         }}

@app.get("/avg_death/")
def avg_death(year:int = None):
    """
    will show the avg death
    parameters 
    - year
    returns
    - avg death

    responce body example

    {
  "data": {
    "EMRO": 4912291,
   
    }
    }
    """
    try:
        global db
        total_deaths = 0
        num_countries = len(getUniqueCountries())

        for row in db:
            total_deaths += int(row[5])

        return total_deaths / num_countries
    
    except Exception as E:
        return {"error": str(E),"success": False,"params":{
              "year": year
         }}





    


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True) #host="127.0.0.1"
