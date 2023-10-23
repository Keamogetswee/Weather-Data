def convert_to_fahrenheit(celsius):
    print("Celsius: " + str(celsius))
    return (celsius * 9/5) + 32

def categorize_weather(temperature_f):
    if temperature_f > 75:
        return 'Warm'
    elif temperature_f < 59:
        return 'Cold'
    else:
        return 'Moderate'
    
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False