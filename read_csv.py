#  function reads weather data from a specified file and processes it to extract the data for further use. 
# It splits the data into header and weather data rows.
# Parameters:
    # file_path: The path to the weather data file to be read.
# Returns:
    # weather_data: A list of lists where each inner list represents a row of weather data.
def read_weather_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [line.strip().split(', ') for line in file.readlines()]
            header = data[0]
            weather_data = data[1:]
        return weather_data
    except FileNotFoundError:
        raise FileNotFoundError("The specified file does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {str(e)}")