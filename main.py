import json
import requests


# ***** FUNCTIONS TO REQUEST API DATA ******

#Function to request API data from the server/database to get available lessons by day.
def get_availability_by_day(string_date):
    result = requests.get(
        'http://127.0.0.1:5002/availability/{}'.format(string_date),
        headers={'content-type': 'application/json'}
    )
    return result.json()

#Function to request API data from the server/database to get available lessons by time.
def get_availability_by_time(time):
    result = requests.get(
        'http://127.0.0.1:5002/booking/{}'.format(time),
        headers={'content-type': 'application/json'}
    )
    return result.json()  

#Function to request API data from the server/database to get all bookings for a specific customer.
def get_bookings_by_customer(customer_first_name, customer_last_name):
    result = requests.get(
        'http://127.0.0.1:5002/customer/{customer_first_name}/{customer_last_name}'.format(customer_first_name = customer_first_name, customer_last_name = customer_last_name),
        headers={'content-type': 'application/json'}
    )
    return result.json()

# ****** FUNCTIONS TO SEND API DATA ******

#Function to put API data onto the server to allow a customer to book a lesson in the database.
def add_new_booking(json_booking):
    headers={'content-type': 'application/json'}
    url = 'http://127.0.0.1:5002/lessonbooking'
    result = requests.put(url, headers = headers, data = json_booking)
    if result.status_code == 200:
        print("Booking is Successful")
        run()
    else:
        print("Something went wrong, please try again")
        run()

#Function to put API data onto the server to allow a new customer to be added in the database.
def add_new_customer(new_customer_json):
    headers={'content-type': 'application/json'}
    url = 'http://127.0.0.1:5002/newcustomer'
    result = requests.put(url, headers = headers, data = new_customer_json)
    if result.status_code == 200:
        print("Welcome - we have added you to our records.")
        print("You can now book a lesson!")
        run()
    else:
        print("Something went wrong, please try again")
        run()

#Function to put API data onto the server to allow a customer to delete a lesson in the database.
def delete_booking(delete_booking_json):
    headers={'content-type': 'application/json'}
    url = 'http://127.0.0.1:5002/deletelesson'
    result = requests.put(url, headers = headers, data = delete_booking_json)
    if result.status_code == 200:
        print("Cancellation was successful")
        run()
    else:
        print("Something went wrong, please try again")
        run()

#Function to put API data onto the server to allow a customer to message a teacher.
def message_teacher(message_json):
    headers={'content-type': 'application/json'}
    url = 'http://127.0.0.1:5002/message'
    result = requests.put(url, headers = headers, data = message_json)
    if result.status_code == 200:
        print("Your message was sent")
        run()
    else:
        print("Something went wrong, please try again")
        run()

# ****** FUNCTIONS TO DISPLAY DATA TO THE CUSTOMER ******

#Function to display the availability by date data in a readable format.
def display_availability_date(records):
    # Print the names of the columns.
    print("{:<20} {:<20}".format(
        'Time', 'Teacher'))
    print('-' * 125)
    # Print the data returned from the database.
    for item in records:
        print("{:<20} {:<20}".format(
            item['Time'], item['Teacher']
        ))
        
#Function to display the availability by time data in a readable format.
def display_availability_time(records):
    # Print the names of the columns.
    print("{:<20} {:<20}".format(
        'Date', 'Teacher'))
    print('-' * 125)
    # Print the data returned from the database.
    for item in records:
        print("{:<20} {:<20}".format(
            item['Date'], item['Teacher']
        ))

#Function to display a customer's current bookings in a readable format.
def display_availability_current_bookings(records):
    # Print the names of the columns.
    print("{:<20} {:<20} {:<20}".format(
        'Date', 'Time', 'Teacher'))
    print('-' * 125)
    # Print the data returned from the database.
    for item in records:
        print("{:<20} {:<20} {:<20}".format(
           item['Date'], item['Time'], item['Teacher']
        ))

# ****** FUNCTIONS TO PROCESS USER INTERACTIONS ******

#Function to set up a new customer.
def new_customer_information():
    # Ask user for their name.
    customer_first_name = input("What is your first name? ")
    customer_last_name = input("What is your second name? ")
    # Turn into JSON format.
    new_customer_json = json.dumps({"customerfirstname":customer_first_name, "customerlastname":customer_last_name})
    #Run function to send information via an API to the database.
    add_new_customer(new_customer_json)

#Function to book a lesson.
def book_new_lesson(string_date, time):
    # Ask user for their name.
    customer_first_name = input("What is your first name? ")
    customer_last_name = input("What is your second name? ")
    # Turn into JSON format.
    booking = {"string_date": string_date, "time": time, "customer_first_name":customer_first_name, "customer_last_name":customer_last_name}
    json_booking = json.dumps(booking)
    # Run function to send information via an API to the database.
    add_new_booking(json_booking)

#Function to retrieve lessons availability:
def retrieve_lesson_availability():
    # Get user information:
    print("We are currently taking bookings for weekdays between 2024-05-01 to 2024-05-17:")
    print("These dates are:")
    print("Wednesday May 1st - Friday May 3rd")
    print("Monday May 6th - Friday May 10th")
    print("Monday May 13th - Friday May 17th")
    print("Our lesson times are:")
    print("09-10, 10-11, 11-12, 14-15, 15-16, 16-17")
    print("All lessons are one hour long")
    search_option = input('Would you like to search by date or time (Date/Time) ?')
    if search_option == "Date":
        string_date = input('What date you would like to book your lesson for (YYYY-MM-DD)?: ')
        # Run function to get availability via an API from the database.
        slots = get_availability_by_day(string_date)
        # Display this information to the user.
        print('************************************************************************')
        print('------------------------------ AVAILABILITY -----------------------------')
        print('************************************************************************')
        print("The lessons with available places on " + string_date + " are:")
        display_availability_date(slots)
        print()
        #Ask if the user would now like to book a lesson
        date_place_booking = input('Would you like to book a lesson (Y/N)?  ')
        if date_place_booking == 'Y' or date_place_booking == 'y':
            time = input('Which time would you like to book? ')
            # Use user information to book new lesson in the database via an API.
            book_new_lesson(string_date, time)
        else:
            run()
    elif search_option == "Time":
        time = input('What time would you like to book your lesson for (XX-XX)?: ')
        print(time)
        # Run function to get availability via an API from the database.
        time_available = get_availability_by_time(time)
        print(time_available)
        # Display this information to the user.
        print('************************************************************************')
        print('------------------------------ AVAILABILITY -----------------------------')
        print('************************************************************************')
        print("The dates with available places at " + time + " are:")
        display_availability_time(time_available)
        print()
        #Ask if the user would now like to book a lesson
        time_place_booking = input('Would you like to book a lesson (Y/N)?  ')
        if time_place_booking == 'Y' or time_place_booking == 'y':
            string_date = input('What date would you like to book your lesson for YYYY-MM-DD?: ')
            # Use user information to book new lesson in the database via an API.            
            book_new_lesson(string_date, time)
        else:
            run()

# ****** FUNCTION TO SIMULATE USER INTERACTION ******

# Function to simulate the online interaction with a customer:
def run():
    print('************************************************************************')
    print('------------------ Welcome to Dolphin Swimming School ------------------')
    print('------------------- Where everyone can learn to swim -------------------')
    print('--- Individual swimming lessons for people of all ages and abilities ---')
    print('------------------ Our mission is to teach YOU to swim -----------------')
    print('************************************************************************')
    print()
    print('Please select from the options below:')    
    print("1. Make A Booking")
    print("2. Check Your Bookings")
    print("3. Cancel A Booking")
    print("4. Send A Message To One Of Our Teachers")
    print()
    option = input("Please Select An Option (1-4): ")  
    # Process information for option 1:
    if option == "1":
        print()
        customer_status = input("Have you set up an account with Dolphin Swimming School (Y/N)? ")
        if customer_status == 'N' or customer_status == 'n':
            # Create a new customer then book lesson
            new_customer_information()
            retrieve_lesson_availability()
        elif customer_status == 'Y' or customer_status == 'y':
            # Run function to book lesson
            retrieve_lesson_availability()
        else:
            run()
    # Process information for option 2:
    elif option == "2":
        print()
        # Get user information.
        customer_first_name = input("What is your first name? ")
        customer_last_name = input("What is your second name? ")
        #Get current bookings from the database via an API and display to the customer.
        current_bookings = get_bookings_by_customer(customer_first_name, customer_last_name)
        print('**************** Your Current Bookings Are ****************')
        display_availability_current_bookings(current_bookings)
        run()
    # Process information for option 3:
    elif option == '3':
        print()
        # Get user information.
        customer_first_name = input("What is your first name? ")
        customer_last_name = input("What is your second name? ")
        #Get current bookings from the database via an API and display to the customer.       
        current_bookings = get_bookings_by_customer(customer_first_name, customer_last_name)
        print('**************** Your Current Bookings Are ****************')
        display_availability_current_bookings(current_bookings)
        # Get user information about which lesson to canel.     
        cancel_date = input("What is the date of the lesson you want to cancel (YYYY-MM-DD)? ")
        cancel_time = input("What is the time of the lesson you want to cancel (XX-XX)? ")
        # Cancel the lesson in the database via an API.
        delete_booking_json = json.dumps({"string_date": cancel_date, "time":cancel_time})
        delete_booking(delete_booking_json)
        print()
        run()
    # Process information for option 4:
    elif option == '4':
        print()
        # Get information from the user.
        lesson_teacher_id = input("Which teacher do you want to send a message to (Becky, Amy, Alex)? ")
        message = input("What is your message? Please include your full name.")
        # Turn user information into JSON file.
        message_json = json.dumps({"lesson_teacher_id":lesson_teacher_id, "message":message})
        # Put the message in the database via an API
        message_teacher(message_json)
        run()
    else:
        run()

if __name__ == '__main__':
    run()
