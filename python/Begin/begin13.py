pi=3.14
r1, r2 = map(int, input("Ikkita doiraning radiuslarini kiriting (R1 > R2): ").split())

s1=pi*(r1**2)
s2=pi*(r2**2)
s3=s1-s2

print("Katta doiraning yuzi: ", s1)
print("Kichik doiraning yuzi: ", s2)
print("Katta doiradan kichigining ayirmasi: ", s3)
