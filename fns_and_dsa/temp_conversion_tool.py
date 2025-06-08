FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            temperature_str = input("Enter the temperature to convert: ")
            temperature = float(temperature_str)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue

    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")

if __name__ == "__main__":
    main()
