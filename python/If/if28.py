y = int(input("Yil raqami kiriting: "))

result = 365

if y%4==0:
  if y%100==0 and y%400!=0:
    pass
  else:
    result=366

print(result)