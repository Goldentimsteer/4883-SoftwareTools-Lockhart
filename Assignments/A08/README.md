A08 - Fast Api with Covid Data

Discription

Create a RESTful API using FastAPI that provides access to COVID-19 data. The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases. Use FastAPI to build the API (code mostly provided) The API should have the endpoints listed in the sections below
Try to handle errors gracefully. For example, if a parameter that is passed in causes an error, simply return {'success':False} or return the parameters passed in as well {'success':False,'param1':value1,'param(n):value(n)}. This helps for debugging. Implement proper API documentation using FastAPI's 
built-in support for OpenAPI (Swagger UI). This means comment your functions using markdown syntax for readability. I'll provide an example below the routes.



##  Assignments Folder

|   #   | File        |Discription             | 
| :---: | ----------- | ---------------------- |
|   1   | [api.py](api.py) |makes a local server to host api server with endpoints to get data |
|  2    | [data.cvs](data.cvs)|data for api|
| 3 | [requirments.txt](requirments.txt)| the requiremtns to run this program|
