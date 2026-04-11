
def IsPalindrome(k):
  return str(k)==str(k)[::-1]

numbers = [32534, 634, 121, 7654567, 436324]
count = 0

for i in numbers: 
  if IsPalindrome(i):
    count+=1
  
print(f"To'plamda {count} ta palindrom bor.")