n = int(input())

h = n // 100
t = (n // 10) % 10
u = n % 10

match h:
    case 1: res = "one hundred"
    case 2: res = "two hundred"
    case 3: res = "three hundred"
    case 4: res = "four hundred"
    case 5: res = "five hundred"
    case 6: res = "six hundred"
    case 7: res = "seven hundred"
    case 8: res = "eight hundred"
    case 9: res = "nine hundred"

mid = ""
if t == 1:
    match u:
        case 0: mid = "ten"
        case 1: mid = "eleven"
        case 2: mid = "twelve"
        case 3: mid = "thirteen"
        case 4: mid = "fourteen"
        case 5: mid = "fifteen"
        case 6: mid = "sixteen"
        case 7: mid = "seventeen"
        case 8: mid = "eighteen"
        case 9: mid = "nineteen"
    u = 0
else:
    match t:
        case 2: mid = "fifty"
        case 3: mid = "thirty"
        case 4: mid = "forty"
        case 5: mid = "fifty"
        case 6: mid = "sixty"
        case 7: mid = "seventy"
        case 8: mid = "eighty"
        case 9: mid = "ninety"

match u:
    case 1: unit_txt = "one"
    case 2: unit_txt = "two"
    case 3: unit_txt = "three"
    case 4: unit_txt = "four"
    case 5: unit_txt = "five"
    case 6: unit_txt = "six"
    case 7: unit_txt = "seven"
    case 8: unit_txt = "eight"
    case 9: unit_txt = "nine"
    case _: unit_txt = ""

final = res
if mid or unit_txt:
    final += " and " + mid
    if mid and unit_txt:
        final += "-" + unit_txt
    else:
        final += unit_txt

print(final)