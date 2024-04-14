def length_conversion(value, source_unit, target_unit):
    if source_unit == "m":
        if target_unit == "cm":
            return value * 100
        elif target_unit == "km":
            return value / 1000
    elif source_unit == "cm":
        if target_unit == "m":
            return value / 100
    elif source_unit == "km":
        if target_unit == "m":
            return value * 1000
    return value


def temperature_conversion(value, source_unit, target_unit):
    if source_unit == "c":
        if target_unit == "f":
            return (value * 9 / 5) + 32
    elif source_unit == "f":
        if target_unit == "c":
            return (value - 32) * 5 / 9
    return value


def weight_conversion(value, source_unit, target_unit):
    if source_unit == "kg":
        if target_unit == "g":
            return value * 1000
        elif target_unit == "lb":
            return value * 2.20462
    elif source_unit == "g":
        if target_unit == "kg":
            return value / 1000
    elif source_unit == "lb":
        if target_unit == "kg":
            return value / 2.20462
    return value


def theMain():
    while True:
        print("Select the type of conversion:")
        print("1. Length")
        print("2. Temperature")
        print("3. Weight")
        conversion_type = input("Enter your choice (1/2/3): ")

        if conversion_type not in ["1", "2", "3"]:
            print("Invalid choice. Please select again.")
            continue

        value = float(input("Enter the value to be converted: "))
        source_unit = input("Enter the source unit: ")
        target_unit = input("Enter the target unit: ")

        if conversion_type == "1":
            result = length_conversion(value, source_unit, target_unit)
            print(f"{value} {source_unit} is equal to {result} {target_unit}")
        elif conversion_type == "2":
            result = temperature_conversion(value, source_unit, target_unit)
            print(f"{value} {source_unit} is equal to {result} {target_unit}")
        elif conversion_type == "3":
            result = weight_conversion(value, source_unit, target_unit)
            print(f"{value} {source_unit} is equal to {result} {target_unit}")



if __name__ == "__main__":
    main()
