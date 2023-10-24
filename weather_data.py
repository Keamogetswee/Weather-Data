# Import mysql.connector
from helper_functions import categorize_weather, convert_to_fahrenheit, isfloat
from database import initialize_db, retrive_specific_data
from process_csv import process_line
from read_csv import read_weather_data
from export_csv import export_to_csv_file

# Initialize the database.
# Read weather data from the 'weather-data.txt' file.
# Process each line of data:
#         - If the line contains less than 5 elements, it is skipped.
#         - Extract the date, city, temperature, humidity, and condition from the line.
#         - If temperature is not numeric, set it to None.
#         - Convert the temperature to Fahrenheit.
#         - Categorize the weather based on temperature.
#         - Process the line and insert the data into the database.
# Retrieve specific data from the database (e.g., data for the city 'Johannesburg').
# Export the retrieved data to a CSV file 'filtered_weather_data.csv'.
# This function serves as the entry point for running the Weather Data.
def main():
    initialize_db()
    retrieved_data = read_weather_data('weather-data.txt')
    for line in retrieved_data:
        if len(line) < 5:
            continue
        date = line[0]
        city = line[1]
        temperature = line[2]
        humidity = line[3]
        condition = line[4]
        
        if not temperature.isnumeric():
            temperature = None

        temperature_fahrenheit = convert_to_fahrenheit(temperature)
        weather_category = categorize_weather(temperature_fahrenheit)
        process_line(date, city, temperature_fahrenheit, humidity, condition, weather_category)
        filtered_data = retrive_specific_data("Johannesburg")
        export_to_csv_file(filtered_data)

# Call the main function
main()
