# Task 1: Read from a file
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