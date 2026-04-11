def RectPS(x1, y1, x2, y2):
  width = abs(x1-x2)
  height = abs(y1-y2)

  p = 2*(width+height)
  s = width*height
  return p, s

rectangles = [
    (0, 0, 4, 3),   # 1-to'rtburchak
    (-2, -2, 2, 2), # 2-to'rtburchak
    (1.5, 2.5, 5.0, 6.0) # 3-to'rtburchak
]

for i in rectangles:
  print(RectPS(*i))