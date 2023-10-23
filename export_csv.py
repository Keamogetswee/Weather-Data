import csv


def export_to_csv_file(data):
    with open('filtered_weather_data.csv','w') as csvfile:
        write_to_csv = csv.writer(csvfile)
        write_to_csv.writerow(['Date', 'City', 'TemperatureC', 'HumidityPercent', 'Condition', 'Weather_Type'])
        write_to_csv.writerows(data)