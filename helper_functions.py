# function converts a temperature value from degrees Celsius to degrees Fahrenheit.
# It applies the formula for temperature conversion and returns the result in Fahrenheit.
def convert_to_fahrenheit(celsius):
    if celsius is None:
        return 
    else:
        return (int(celsius) * 9/5) + 32

# categorizes a temperature value into weather types, such as "Warm," "Cold," or "Moderate,"
# based on specific temperature thresholds. 
def categorize_weather(temperature_f):
    if temperature_f is None:
        return
    if temperature_f > 75:
        return 'Warm'
    elif temperature_f < 59:
        return 'Cold'
    else:
        return 'Moderate'

# function checks whether a given value is a valid floating-point number.
# It returns True if successful
# If the conversion fails, it returns False    
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False