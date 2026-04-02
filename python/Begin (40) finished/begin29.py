degree = int(input("Burchak o'lchovini kiriting (0≤x<360): "))

def intacter2(num):
  return (int(num*100))/100

print(f"{degree} gradus = {intacter2(degree/180)} radian")