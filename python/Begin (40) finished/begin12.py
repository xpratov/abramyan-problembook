a, b = map(int, input("To'g'ri burchakli uchburchakning katetlarini kiriting: ").split())

hypo = (a*a+b*b)**(1/2)
print("Uchburchakning gipotenuzasi: ", hypo)
print("Uchburchakning perimetri: ", a+b+hypo)