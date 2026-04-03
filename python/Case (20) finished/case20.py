d = int(input())
m = int(input())

match m:
    case 1:
        res = "Capricorn" if d < 20 else "Aquarius"
    case 2:
        res = "Aquarius" if d < 19 else "Pisces"
    case 3:
        res = "Pisces" if d < 21 else "Aries"
    case 4:
        res = "Aries" if d < 20 else "Taurus"
    case 5:
        res = "Taurus" if d < 21 else "Gemini"
    case 6:
        res = "Gemini" if d < 22 else "Cancer"
    case 7:
        res = "Cancer" if d < 23 else "Leo"
    case 8:
        res = "Leo" if d < 23 else "Virgo"
    case 9:
        res = "Virgo" if d < 23 else "Libra"
    case 10:
        res = "Libra" if d < 23 else "Scorpio"
    case 11:
        res = "Scorpio" if d < 22 else "Sagittarius"
    case 12:
        res = "Sagittarius" if d < 22 else "Capricorn"

print(res)