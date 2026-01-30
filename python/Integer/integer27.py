k = int(input("Yilning nechanchi kuni? - "))

week = {
  1: "Monday",
  2: "Tuesday",
  3: "Wednesday",
  4: "Thursday",
  5: "Friday",
  6: "Saturday",
  7: "Sunday"
}

qolgan = (k+5)%7 or 7

print(week[qolgan])

