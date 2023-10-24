import csv

# function exports a list of weather data to a csv file named "filtered_weather_data.csv." 
# it writes a header row containing column names, and then writes the weather data records to the file.
# Parameters:
    # data
    # A list of weather data to be exported to the CSV file. 
    # Each element of the list should represent a single data record with the following order: [Date, City, TemperatureC, HumidityPercent, Condition, Weather_Type].
def export_to_csv_file(data):
    with open('filtered_weather_data.csv','w') as csvfile:
        write_to_csv = csv.writer(csvfile)
        write_to_csv.writerow(['Date', 'City', 'TemperatureC', 'HumidityPercent', 'Condition', 'Weather_Type'])
        write_to_csv.writerows(data)