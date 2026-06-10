#1.
#S0 = u0 = 1
#S1 = u0 + u1 = 1 + 11/3 = 14/3
#S2 = u0 + u1 + u2 = S1 + u2 = 14/3 + 73/17 = 457/51

#2.
u = 1
s = u
i = 0
n = int(input("Entrer un nombre: "))

while i < n:
    i = i + 1
    u = 5 - 4 / (u + 2)
    s = s + u

print(s)
