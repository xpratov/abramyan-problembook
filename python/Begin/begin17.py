a, b, c = map(int, input("Sonlar o'qidagi A, B, C nuqtalarni kiriting: ").split())

ac = abs(a-c)
bc = abs(b-c)
print(f"AC {ac}ga teng.\nBC {bc}ga teng.\nAC va BC larning yig'indisi {ac+bc}ga teng.")