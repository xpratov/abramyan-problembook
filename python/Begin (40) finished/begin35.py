v, u, t1, t2 = map(int, input("V, U, T1, T2 - kema tezligi, daryo tezligi, T1 soat, T2 soat qiymatlarini kiriting: ").split())

s1=t1*v
s2=(v-u)*t2

s=s1+s2

print(s)