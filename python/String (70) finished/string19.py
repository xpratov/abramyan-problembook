s = input("Satrni kiriting: ")

if s.isdigit() or (s.startswith('-') and s[1:].isdigit()):
    print(1)
else:
    try:
        val = float(s)
        if '.' in s and val != int(val):
            print(2)
        elif '.' in s and val == int(val):
            print(1) 
        else:
            print(0)
    except ValueError:
        print(0)