import mysql.connector

from helper_functions import isfloat


db = mysql.connector.connect(
host="localhost",

database="WeatherTechDB"
)
# Create a cursor
mycursor = db.cursor()

# function is responsible for initializing the database and creating the necessary table,
# It opens a connection to the database, 
# creates the table schema, 
# commits the changes, 
# and then closes the database connection.
def initialize_db():
    db._open_connection()
    mycursor = db.cursor()
    # Create the HistoricalWeatherData table if it doesn't exist
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS HistoricalWeatherData (
            id INT AUTO_INCREMENT PRIMARY KEY,
            `Date` DATE,
            City VARCHAR(100),
            TemperatureC VARCHAR(50),
            HumidityPercent VARCHAR(50),
            `Condition` VARCHAR(100),
            Weather_Type VARCHAR(100)
        )
    """)
    # Commit the changes to the database
    db.commit()
   
    # Close the database connection
    db.close()

# function is responsible for inserting a new record into the table in the database.
# It opens a connection to the database, 
# creates a cursor, 
# defines the INSERT query, 
# executes the query with provided data, 
# commits the changes, and then closes the database connection.
def insert_data(date, city, temperature, humidity, condition, category):
    db._open_connection()
    mycursor = db.cursor()

    # Define the INSERT query
    insert_query = """
    INSERT INTO HistoricalWeatherData (Date, City, TemperatureC, HumidityPercent, `Condition`, Weather_Type)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

    data_ = (date, city, temperature, humidity, condition, category)
    mycursor.execute(insert_query, data_)
    
    db.commit()
    # Close the database connection
    db.close()

# function is responsible for retrieving and displaying all records from the table in the database.
# It opens a connection to the database, 
# creates a cursor, 
# executes a SELECT query to fetch all records
def retrive_all_data():
    db._open_connection()
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM HistoricalWeatherData")
    for i in mycursor:
        print(i)
    db.commit()
   
    # Close the database connection
    db.close()

# function retrieves weather data for a specific city from the table in the database.
# It opens a connection to the database,
# executes an SQL SELECT query to fetch records for the specified city,
# and returns the data as a list of records.
def retrive_specific_data(city):
    db._open_connection()
    mycursor = db.cursor()
    mycursor.execute("SELECT `Date`, City, TemperatureC, HumidityPercent, `Condition`, Weather_Type FROM HistoricalWeatherData WHERE City ='" + city + "'")
    data = mycursor.fetchall()
    average_temp(data)
    return data

def average_temp(data):
    total_temp = 0
    total_hum = 0
    total = len(data)

    for item in data:
            temp = item[2]
            hum = item[3]
            if temp is not None and isfloat(temp) and hum is not None and isfloat(hum):
            # if temp is not None and hum is not None:
            #     if isfloat(temp) and isfloat(hum):
                    total_temp += float(temp)
                    total_hum += float(hum)

    avg_temp = round(total_temp / total, 2) if total > 0 else 0
    avg_hum = round(total_hum / total, 2) if total > 0 else 0
    print(f"Average Temperature: {avg_temp}\nAverage Humidity: {avg_hum}")

    return data




