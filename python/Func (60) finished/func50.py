
def TimeToHMS(t):
  s = t%60
  t //= 60
  m = t%60
  t //= 60
  return h, m, s

times = [400, 3661, 7200, 120, 86400]

for t in times:
    h, m, s = TimeToHMS(t)
    print(f"{t:<10} | {h} soat, {m} min, {s} sek")