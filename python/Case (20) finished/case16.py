n = int(input("Enter an age (20-69): "))

if 20 <= n <= 69:
    tens = n // 10
    units = n % 10

    match tens:
        case 2: tens_text = "twenty"
        case 3: tens_text = "thirty"
        case 4: tens_text = "forty"
        case 5: tens_text = "fifty"
        case 6: tens_text = "sixty"
        case _: tens_text = ""

    match units:
        case 1: units_text = "one"
        case 2: units_text = "two"
        case 3: units_text = "three"
        case 4: units_text = "four"
        case 5: units_text = "five"
        case 6: units_text = "six"
        case 7: units_text = "seven"
        case 8: units_text = "eight"
        case 9: units_text = "nine"
        case _: units_text = ""

    if units == 0:
        result = f"{tens_text} years"
    else:
        result = f"{tens_text}-{units_text} years"
    
    print(result)

else:
    print("Error! Please enter an integer between 20 and 69.")