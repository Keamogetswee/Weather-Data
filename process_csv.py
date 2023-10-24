from database import insert_data
from helper_functions import isfloat

# function processes weather data, 
# including its date, city, temperature, humidity, condition, and a categorized weather type.
# It performs several tasks like validation, transformation, and insertion into a database. 
def process_line(date, city, temperature, humidity, condition, weather_category):
    print(date, city, temperature, humidity, condition, weather_category)
    if not city:
        city = None

    if not temperature or not isfloat(temperature):
        temperature = None
        
    if not humidity:
        humidity = None
        
    if not condition:
        condition = None

    # Insert data into the database
    insert_data(date, city, temperature, humidity, condition, weather_category)
        