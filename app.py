from flask import Flask, jsonify, request
import json
from db_utils import get_all_availability_date, get_all_availability_time, add_booking, get_all_customer_bookings, add_customer, remove_booking, create_message

#Set up app to run the Flask server
app = Flask(__name__)

#Function to listen for a request for API data from the main file for availiilty data by date.
@app.route('/availability/<string_date>')
def get_date_bookings(string_date):
    #Runs the get_all_availability-date function in db_utils to get the requested data from the database.
    res = get_all_availability_date(string_date)
    print(res)
    #Returns JSON data to the URL.
    return jsonify(res)

#Function to listen for a request for API data from the main file for availiilty data by time.
@app.route('/booking/<time>')
def get_time_bookings(time):
    #Runs the get_all_availability-date function in db_utils to get the requested data from the database.
    res = get_all_availability_time(time)
    print(res)
    #Returns JSON data to the URL.
    return jsonify(res)

#Function to listen for a request for API data from the main file for bookings made by a specific customer.
@app.route('/customer/<customer_first_name>/<customer_last_name>')
def get_customer_bookings(customer_first_name, customer_last_name):
    #Runs the get_all_customer_bookings function in db_utils to get the requested data from the database.
    res = get_all_customer_bookings(customer_first_name, customer_last_name)
    print(res)
    #Returns JSON data to the URL.
    return jsonify(res)


#Function to listen for API data being put onto the server for the customer to book a lesson.
@app.route('/lessonbooking', methods=['PUT'])
def book_appt():
    #Get the JSON data from the server.
    booking = request.get_json()
    #Process the JSON data into variables.
    string_date = str(booking['string_date'])
    customer_first_name = str(booking['customer_first_name'])
    customer_last_name = str(booking['customer_last_name'])
    time = str(booking['time'])
    #Call the function from db_utils to process the data into the database
    add_booking(string_date, time, customer_first_name, customer_last_name)
    return booking
  

#Function to listen for API data being put onto the server to add a customer to the database.
@app.route('/newcustomer', methods=['PUT'])
def add_new_customer():
    #Get the JSON data from the server.
    new_customer_data = request.get_json()
    #Process the JSON data into a Python variables.
    customer_first_name= str(new_customer_data['customerfirstname'])
    customer_last_name = str(new_customer_data['customerlastname'])
    #Call the function from db_utils to process the data into the database.
    add_customer(customer_first_name, customer_last_name)
    return new_customer_data

#Function to listen for API data being put onto the server to delete a lesson.
@app.route('/deletelesson', methods=['PUT'])
def cancel_lesson():
    #Get the JSON data from the server.
    booking = request.get_json()
    #Process the JSON data into variables.
    date = booking['string_date']
    time = booking['time']
    #Call the function from db_utils to process the data into the database.
    remove_booking(date, time)
    return booking

#Function to listen for API data being put onto the server to message a teacher.
@app.route('/message', methods=['PUT'])
def message_to_teacher():
    #Get the JSON data from the server.
    booking = request.get_json()
    #Process the JSON data into variables.
    lesson_teacher_id = booking['lesson_teacher_id']
    message = booking['message']
    #Call the function from db_utils to process the data into the database.
    create_message(lesson_teacher_id, message)
    return booking

if __name__ == '__main__':
    app.run(debug=True, port=5002)