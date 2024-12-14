def unit_converter():
    print("1. Celsius to Fahrenheit  2. Kilometers to Miles  3. Kilograms to Pounds")
    choice = input("Enter choice (1/2/3): ")
    value = float(input("Enter value to convert: "))
    
    if choice == '1':
        print(f"{value} °C = {(value * 9/5) + 32} °F")
    elif choice == '2':
        print(f"{value} km = {value * 0.621371} miles")
    elif choice == '3':
        print(f"{value} kg = {value * 2.20462} lbs")
    else:
        print("Invalid choice.")

unit_converter()
