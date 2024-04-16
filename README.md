# This document contains details on how to run the Dolphin Swim School API files

## Introduction

The files in the repository are designed to mimic the API interaction between the customers and database of a swimming school.
The school provides one to one lessons to help people learn to swim, and to improve their abilities.

The APIs allow customers to query information about available lessons and their own bookings in the database.
They then also allow customers to interact with the database to open an account, book lessons, cancel lessons and send messages to the teachers.

The customer's computer (client) and the school's computer (server) communicate via APIs, which allow data to be transfered between them.

### How to edit the config file

In order to work, the db_utils file needs to access mySQL on your local machine.\
To do this it needs your mySQL username, password and host from the mySQL login screen.\
Please update the variables below in the config file before running the other files.

HOST = "XXX"\
USER = "XXX"\
PASSWORD = "XXX"

### Installation requirements

The following packages need to be installed in your virtul environment before running the files:

blinker==1.7.0\
certifi==2024.2.2\
charset-normalizer==3.3.2\
click==8.1.7\
distlib==0.3.8\
filelock==3.13.4\
Flask==3.0.3\
idna==3.7\
itsdangerous==2.1.2\
Jinja2==3.1.3\
MarkupSafe==2.1.5\
mysql-connector-python==8.3.0\
platformdirs==4.2.0\
requests==2.31.0\
simplejson==3.19.2\
urllib3==2.2.1\
virtualenv==20.25.1\
Werkzeug==3.0.2

### How to run the code

1. Run the dolphin.sql file in mySQL to create the database that the Python files interact with.
2. Set up a virtual environment with the packages listed above available within it via the terminal.
3. Open the four files:\
-config.py\
-db_utils.py\
-app.py\
-main.py
4. Ensure that all the modules have correctly been imported at the top of each file (except config).
5. Run app.py to set up the server environment.
6. Run main.py **in a separate terminal window**, to ensure that app.py is still running.
7. Follow the instructions in the terminal window.


### What is supposed to happen when the file runs

When the main.py file loads there are four options that a user can select.
The way these paths can be followed and the use of APIs in the interactions are outlined in the attached **FlowChart.png** file.

There are seven different interactions that use APIs to communicate between the client side (in main.py), via the server(in app.py), to the database (in db_utils.py). The way these seven interactions work are outlined individually below. Each line is prefaced with which side is involved, either client or server.


#### One: Create a new customer

1. **CLIENT**: The customer types their first and second name into the interface. They are turned into JSON format and PUT on the URL ending **/new customer** as an API.
2. **SERVER**: The @app.route decorator attached to the **add_new_customer** function listens for new customer API data being "PUT" onto the URL. The data is retrieved and passed to the **add_customer** function from the db_utils file, which creates the mySQL INSERT to insert the new customer in the database.\
   *INSERT INTO customers (customer_first_name, customer_last_name) VALUES ("Alice",'"Flynn")*
3. **CLIENT**: The programme checks that the update was succesful and prints a message to the customer.

#### Two: Return availiable lessons by time

1. **CLIENT**: The customer types in the time they want to book a lesson, and the programme requests the available lessons for this time as an API from the **/booking** URL.
2. **SERVER**: The @app.route decorator attached to the **get_time_bookings** function listens for a request for an API on the URL and runs the **get_all_availability_time** function from db_utils, which creates the mySQL query to get the information requested by the customer.    
   *SELECT Date, Teacher FROM full_available_lesson_data WHERE Time = "11-12";*
3. **SERVER**: The function appends all the records into a list and it is turned into JSON and put onto the URL as an API.
4. **CLIENT**: The programme receives the API and the data is then processed so it can be read by the customer.

#### Three: Return availiable lessons by date

1. **CLIENT**: The customer types in the date they want to book the lesson and the programme requests the availalble lessons on this date as an API from the **/availiablility** URL.
2. **SERVER**: The @app.route decorator attached to the **get_date_bookings** function listens for a request for an API on the URL. It then runs the **get_all_availability_date** function from db_utils, which creates the mySQL query to get the information requested by the customer.   
   *SELECT Time, Teacher FROM full_available_lesson_data WHERE Date = "2024-05-01";*
3. **SERVER**: The function appends all the records into a list and it is turned into JSON and put onto the URL as an API.
4. **CLIENT**: The programme receives the API and the data is then processed so it can be read by the customer.

#### Four: Book a lesson

1. **CLIENT:** When the programme has the date and time of the new lesson it calls the **book_new_lesson** function. The function asks for the customer's first and last name and creates a JSON format of the data which is put on the **/lessonbooking** URL as an API.
2. **SERVER** The @app.route decorator listens for an API "PUT" on this URL. It calls the **add_booking** function from db_utils, which creates the UPDATE statement in mySQL that will add the booking, after first getting the customer_id and the lesson_time_id.\
    *UPDATE lessons SET customer_id = 4 WHERE lesson_date = "2024-05-01 AND lesson_time_id = 1*
3. **CLIENT**: The programme checks that the update was succesful and prints a message to the customer.

#### Five: Return current bookings

1. **CLIENT**: The customer types their first and second name into the interface. This is turned into an API request for all current bookings on the URL ending **customer/{customer_first_name}/{customer_last_name}**.
2. **SERVER**: The @app.route decorator attached to the **get_customer_bookings** function listens for the API request.  It then calls the **get_all_customer_bookings** function from db_utils file, which creates the query for the mySQL database.\
   *SELECT Time, Teacher, Date FROM full_lesson_data WHERE FirstName = "Alice" AND LastName = "Flynn"*
3. **SERVER**: The function appends all the records into a list and it is turned into JSON and put onto the URL as an API.
4. **CLIENT**: The programme receives the API and the data is then processed so it can be read by the customer.

#### Six: Cancel a booking

1. **CLIENT**: The above steps in interaction five are performed, so the customer can see their currently booked lessons.
2. **CLIENT**: The customer then enters the date and time of the lesson they want cancel. This is turned into JSON data and put on the **/deletelesson** URL as an API.
3. **SERVER**: The @app.route decorator on the **cancel_lesson** function listens for the API being sent. The function **remove_booking** is called in db-utils, which creates the mySQL UPDATE to cancel the booking, after getting the id number of the time.\
   *UPDATE lessons SET customer_id = NULL WHERE lesson_date = "2024-05-01" AND lesson_time_id = 2*
4. **CLIENT**: The programme checks that the update was succesful and prints a message to the customer.

#### Seven: Send a message

1. **CLIENT**: The customer types in the teacher they want to message and the message they want to send.  This is turned into JSON format and put onto the URL **/message** as an API.
2. **SERVER**: The @app.route decorator attached to the **message_to_teacher** function listens for the API.  It calls the **create_message** function in db_utils, which creates the INSERT statement for mySQL, after getting the teacher's id.\
   *INSERT INTO messages (lesson_teacher_id, message) VALUES (1, "I am running late today - Alice")*
3. **CLIENT**: The programme checks that the update was succesful and prints a message to the customer.
        
