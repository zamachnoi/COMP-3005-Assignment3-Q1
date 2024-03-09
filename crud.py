import psycopg2

# Hardcoded database connection, change if needed
db_host = "localhost"
db_port = "5432"
db_name = "postgres"
db_user = "postgres"
db_password = "test"

# Connect to your postgres DB
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Open a cursor to perform database operations
curs = conn.cursor()


# Helper function to print all data in a dictionary
def printAllStudents(columnData):
    # get the max length of each column
    columnWidths = {}

    # check each value in each column and get the max length
    columnWidths = {key: max(len(str(val)) for val in columnData[key]) for key in columnData}

    # check each key and get the max length
    columnWidths = {key: max(len(key), columnWidths[key]) for key in columnData}

    # print the column names
    for key in columnData:
        print(format(key, f"{columnWidths[key]}s"), end=" ")
    print()

    # Get the keys (column names) from the dictionary
    keys = list(columnData.keys())

    # Go through each row and print the data
    for i in range(len(columnData[keys[0]])):
        for key in columnData:
            print(format(str(columnData[key][i]), f"{columnWidths[key]}s"), end=" ")
        print()


# use cursor to READ all students
def getAllStudents():
    # array to store column names
    columnNames = []
    # dictionary to store column data
    columnData = {}

    # execute the query
    curs.execute('SELECT * FROM students ORDER BY student_id ASC')

    # get the column names
    for desc in curs.description:
        columnNames.append(desc[0])

    # initialize the dictionary with empty lists for data in each column
    for column in columnNames:
        columnData[column] = []
    
    # fetch all the rows
    rows = curs.fetchall()

    # go through rows and add data to the dictionary
    for row in rows:
        for i in range(len(columnNames)):
            columnData[columnNames[i]].append(row[i])

    # print the data
    printAllStudents(columnData)

    # return the data
    return columnData

def addStudent(first_name, last_name, email, enrollment_date):
    # try to insert the student using cursor and given data
    try:
        curs.execute('INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)', (first_name, last_name, email, enrollment_date))
        conn.commit()
        return True
    # if there is an error, rollback the transaction
    except Exception as e:
        conn.rollback()
        raise e

def updateStudentEmail(student_id, new_email):
    # try to update the student email using cursor and given data
    try:
        curs.execute('UPDATE students SET email = %s WHERE student_id = %s', (new_email, student_id))
        conn.commit()
        return True
    # if there is an error, rollback the transaction
    except Exception as e:
        conn.rollback()
        raise e

def deleteStudent(student_id):
    # try to delete the student using cursor and given data
    try:
        curs.execute('DELETE FROM students WHERE student_id = %s', (student_id,))
        conn.commit()
        return True
    # if there is an error, rollback the transaction
    except Exception as e:
        conn.rollback()
        raise e

# loop flag
loop = True
while loop:
    # print the menu
    print("Student Management System")
    print("Enter number for action:\n1. Add Student\n2. Update Student Email\n3. Delete Student\n4. Get All Students\n0. Exit\n")

    # get user input for selection
    userSelect = input("Selection: ")
    print()

    # try to perform the action based on user input
    try:
        if userSelect == "1":
            print("Add Student")

            # user data input
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date: ")

            addStudent(first_name, last_name, email, enrollment_date)

        elif userSelect == "2":
            print("Update Student Email")

            # id to update, and email to update to
            student_id = input("Enter student id: ")
            new_email = input("Enter new email: ")

            updateStudentEmail(int(student_id), new_email)

        elif userSelect == "3":
            print("Delete Student")

            #id to delete
            student_id = input("Enter student id: ")

            deleteStudent(int(student_id))
        elif userSelect == "4":
            print("Get All Students")

            getAllStudents()
        elif userSelect == "0":
            # exit the loop
            print("Exiting...")
            loop = False
        else:
            # invalid input, next loop
            print("Invalid input, please enter a number between 0 and 4")
        print()
    except Exception as e:
        print(f"\nERROR: {e}")



# close the cursor and connection
curs.close()
conn.close()
