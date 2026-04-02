n = input("To'rt xonali son kiriting: ")

print(n, "sonini chapdan o'nga o'qisangiz ham, o'ngdan chapga o'qisangiz ham bir xil?")
if n==n[::-1]:
  print(True)
else:
  print(False)