n = input("Uch xonali son kiriting: ")

print(n, "sonining raqamlari o'sib borish yoki kamayib borish tartibida joylashgan?")
n1=int(n[0])
n2=int(n[1])
n3=int(n[2])
if n1<n2<n3 or n1>n2>n3:
  print(True)
else:
  print(False)