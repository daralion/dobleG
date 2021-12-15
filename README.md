# dobleG

WebApp that shows graphs for data based on the apis available in https://api-doc.getonbrd.com/.

Data from the apis was programatically retrieved and saved in a mongo DB for ease of access.

This data is retrieved by a python app (Django) and graphed. The graphs are displayed in a web app.

# Required modules
Since this is a python app, some modules are required to work. 

These modules can be installed by typing in cmd

> python -m pip install 'module'

The list of required modules is: 

1. pymongo
2. django
3. pandas
4. plotly 

# Get the data

The data is saved into a mongoDB instance. It is expecting a service in localhost:27017.
the database will be created under the 'GoBDB' name

To get the data, run the DbRead/DbRead.py file. 
**This process takes a long time, and has no failsafe**, so beware!


# Run the app
To run the app, go to GoB/dashboard and run
> python manage.py runserver

this runs an instance in localhost:8000

after it is running, open a browser and go to http://localhost:8000/dashboard/

# App functionality

The main dashboard page shows 2 graphs:
 1. The top 10 categories by occurrence with a list of all the categories and occurrences next to it
![dashboardpage](/resources/SS1.png?raw=true "Optional Title")

 2. A pie chart with the % of seniority requested by job
![dashboardpage](/resources/SS2.png?raw=true "Optional Title")


Additionally, if you click the navbar menu to the right, you can select the selection page. 
This page lets you select a category in order to show the seniority % by category
![dashboardpage](/resources/SS3.png?raw=true "Optional Title")
