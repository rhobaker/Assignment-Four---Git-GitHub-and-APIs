import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass

# Function to use the information in dolphin_config to connect to mySQL.
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

# Function to get the customer ID number from the first and second name of the customer.
def get_customer_id(customer_first_name, customer_last_name):
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        #mySQL query to get the customer_id number from the customer_id table.
        customer_id = """SELECT customer_id FROM customers WHERE customer_first_name = '{customer_first_name}' AND customer_last_name = '{customer_last_name}'""".format(customer_first_name = customer_first_name, customer_last_name = customer_last_name)
        #Execute the query.
        cur.execute(customer_id)
        #Extract the customer_id number.
        customerid_result = (cur.fetchall())[0][0]
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return customerid_result

# Function to get the teacher ID number from the teacher's name.
def get_teacher_id(teacher_name):
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        #mySQL query to get the lesson_teacher_id number from the teachers table.
        teacher_id = """SELECT lesson_teacher_id FROM teachers WHERE teacher_name = '{teacher_name}'""".format(teacher_name = teacher_name)
        #Execute the query.
        cur.execute(teacher_id)
        #Extract the teacher_id number.
        teacher_id_result = (cur.fetchall())[0][0]
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return teacher_id_result

# Function to get the lesson_time_id number from the time string.
def get_lesson_time_id(time):
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        #mySQL query to get the lesson_time_id number from the lesson_time_id table.
        lesson_time_id = """SELECT lesson_time_id FROM lessons_times WHERE lesson_time = '{time}'
        """.format(time = time)
        #Execute the query
        cur.execute(lesson_time_id)
        #Get the result
        lessonid_result = (cur.fetchall())[0][0]
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return lessonid_result

#Function to get all lessons available on a selected date.
def get_all_availability_date(string_date):
    availability = []
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        #mySQL query to select the time and teacher for avaliable lessons on the selected date.
        #Using the full_available_lesson_data view.
        query = """
            SELECT Time, Teacher
            FROM full_available_lesson_data
            WHERE Date = '{}'
            """.format(string_date)
        #Execute the query
        cur.execute(query)
        #Get the result of the query
        result = cur.fetchall()
        cur.close()
        #Create a list of the returned data
        for item in result:
            availability.append({
            'Time': item[0],
            'Teacher': item[1],
        })
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return availability

#Function to get all lessons available for a selected time.
def get_all_availability_time(time):
    availability = []
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        #mySQL query to select the date and teacher for avaliable lessons at a selected time.
        #Using the full_available_lesson_data view.
        query = """
            SELECT Date, Teacher
            FROM full_available_lesson_data
            WHERE Time = '{}'
            """.format(time)
        #Execute the query
        cur.execute(query)
        #Get the result of the query
        result = cur.fetchall()
        cur.close()
        #Create a list of the returned data
        for item in result:
            availability.append({
                'Date': item[0],
                'Teacher': item[1],
        })
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return availability


#Function to get all the bookings that a specific customer has made
def get_all_customer_bookings(customer_first_name, customer_last_name):
    all_bookings = []
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        #mySQL query to get any bookings from the full_lesson_data view.
        query = """
            SELECT Time, Teacher, Date
            FROM full_lesson_data
            WHERE FirstName = '{customer_first_name}' AND LastName = '{customer_last_name}'
            """.format(customer_first_name = customer_first_name, customer_last_name = customer_last_name)
        #Execute query
        cur.execute(query)
        #Get the result of the query
        bookings = cur.fetchall()
        cur.close()
        #Append all results together
        for item in bookings:
            all_bookings.append({
                'Date': item[2],
                'Time': item[0],
                'Teacher': item[1],
            })
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return all_bookings

#Function to add a booking to the database
def add_booking(string_date, time, customer_first_name, customer_last_name):
    #Get the customer_id from the inputs
    customer_id = get_customer_id(customer_first_name, customer_last_name)
    lesson_time_id = get_lesson_time_id(time)
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        #mySQL query to update the lessons table
        query = """
            UPDATE lessons
            SET 
            customer_id = '{customer_id}'
            WHERE lesson_date = '{string_date}' AND lesson_time_id = '{lesson_time_id}'
            """.format(customer_id = customer_id, string_date = string_date, lesson_time_id = lesson_time_id)
        #Execute the query
        cur.execute(query)
        #Commit the changes to the database
        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

#Function to delete a booking when a customer wants to cancel
def remove_booking(string_date, time):
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        lesson_time_id = get_lesson_time_id(time)
        #mySQL query to update the customer_id to null to cancel a booking
        query = """
            UPDATE lessons
            SET 
            customer_id = NULL
            WHERE lesson_date = '{string_date}' AND lesson_time_id = '{lesson_time_id}'
            """.format(lesson_time_id = lesson_time_id, string_date = string_date)
        #Execute the query
        cur.execute(query)
        #Commit the changes in the database
        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

#Function to add a customer to the customers table, to allow them to book a lesson
def add_customer(customer_first_name, customer_last_name):
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        #mySQL query to insert into the customers table
        new_customer_query = """INSERT INTO customers (customer_first_name, customer_last_name) VALUES ('{customer_first_name}','{customer_last_name}')""".format(customer_first_name = customer_first_name, customer_last_name = customer_last_name)
        #Execute the query
        cur.execute(new_customer_query)
        #Commit the changes to the database
        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

#Function to create a message for a teacher
def create_message(lesson_teacher, message):
    try:
        #Connect to the database
        db_name = 'dolphin_swim_school'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        lesson_teacher_id = get_teacher_id(lesson_teacher)
        #mySQL query to insert into the customers table
        new_message_query = """INSERT INTO messages (lesson_teacher_id, message) VALUES ('{lesson_teacher_id}','{message}')""".format(lesson_teacher_id = lesson_teacher_id, message = message)
        #Execute the query
        cur.execute(new_message_query)
        #Commit the new message to the database
        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

if __name__ == '__main__':
     get_customer_id("Julia", "Chapman")
#     get_lesson_time_id("10-11")
#     create_message(1, "Hello, World!")
#     get_all_availability_date("2024-05-02")
#     get_all_availability_time("11-12")
#     get_all_customer_bookings("Julia", "Chapman")
    # add_booking("2024-05-03","09-10","Victoria", "Beckham")
    # remove_booking("2024-05-03","09-10")
    # add_customer("Emily", "Pankhurst")
