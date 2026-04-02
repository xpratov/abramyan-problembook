k = int(input("Yilning nechanchi kuni? - "))

week = {
  0: "Sunday",
  1: "Monday",
  2: "Tuesday",
  3: "Wednesday",
  4: "Thursday",
  5: "Friday",
  6: "Saturday"
}

qolgan = (k+3)%7

print(week[qolgan])