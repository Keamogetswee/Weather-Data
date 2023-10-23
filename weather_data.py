# Import mysql.connector
from helper_functions import categorize_weather, convert_to_fahrenheit, isfloat
from database import initialize_db, retrive_specific_data
from process_csv import process_line
from read_csv import read_weather_data
from export_csv import export_to_csv_file

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
            continue
        # print(temperature.isnumeric())
        # Convert temperature to Fahrenheit and categorize the weather
        temperature_fahrenheit = convert_to_fahrenheit(int(temperature))
        weather_category = categorize_weather(temperature_fahrenheit)
        process_line(date, city, temperature_fahrenheit, humidity, condition, weather_category)
        filtered_data = retrive_specific_data("Johannesburg")
        export_to_csv_file(filtered_data)
        
        

# Call the main function
main()
