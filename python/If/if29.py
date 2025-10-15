n = int(input("Butun son kiriting: "))

result = " number"

if n!=0:
  if n%2==0:
    result=" even"+result
  else:
    result=" odd"+result
  if n<0:
    result="negative"+result
  else:
    result="positive"+result
else:
  result="zero"+result
print(result)