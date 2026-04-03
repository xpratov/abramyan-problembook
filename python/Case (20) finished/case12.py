import math as m
order = int(input("Elementning tartib raqamini kiriting (1,2,3,4.): "))
value = float(input(f"{order}-elementning qiymatini kiriting: "))

pi=3.14

match order:
  case 1:
    print("Radius: ", value)
    print("Diametr: ", value*2)
    print("Aylana uzunligi: ", 2*pi*value)
    print("Yuzi: ", pi*value**2)
  case 2:
    print("Radius: ", value/2)
    print("Diametr: ", value)
    print("Aylana uzunligi: ", pi*value)
    print("Yuzi: ", pi*(value/2)**2)
  case 3:
    print("Radius: ", value/(2*pi))
    print("Diametr: ", value/pi)
    print("Aylana uzunligi: ", value)
    print("Yuzi: ", (value**2)/(4*pi))
  case 4:
    print("Radius: ", m.sqrt(value/pi))
    print("Diametr: ", m.sqrt(value/pi)*2)
    print("Aylana uzunligi: ", m.sqrt(value/pi)*2*pi)
    print("Yuzi: ", value)
