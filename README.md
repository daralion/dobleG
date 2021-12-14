# dobleG

WebApp that shows graphs for data based on the apis available in https://api-doc.getonbrd.com/.

Data from the apis was programatically retrieved and saved in a mongo DB for ease of access.

This data is retrieved by a python app (Django) and graphed. The graphs are displayed in a web app.

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
