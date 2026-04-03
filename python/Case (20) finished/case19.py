year = int(input())

diff = (year - 1984) % 60
color_idx = (diff // 12) % 5
animal_idx = diff % 12

match color_idx:
    case 0: color = "Green"
    case 1: color = "Red"
    case 2: color = "Yellow"
    case 3: color = "White"
    case 4: color = "Black"

match animal_idx:
    case 0: animal = "Rat"
    case 1: animal = "Cow"
    case 2: animal = "Tiger"
    case 3: animal = "Hare"
    case 4: animal = "Dragon"
    case 5: animal = "Snake"
    case 6: animal = "Horse"
    case 7: animal = "Sheep"
    case 8: animal = "Monkey"
    case 9: animal = "Hen"
    case 10: animal = "Dog"
    case 11: animal = "Pig"

print(f"The {color} {animal}'s year")