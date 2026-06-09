#1.
def u(n):
    if n==0:
        return 2
    else:
        return 3*u(n-1)-2

print(u(0))
print(u(1))
print(u(2))

n=10
print(u(n))

#2.
def u(n):
    if n == 0:
        return 1  # u_0 = 1
    else:
        u_prec = u(n-1)  # On stocke le terme précédent pour éviter les doubles calculs
        return (2 * u_prec**2 + 1) / (u_prec**2 + 1)

# Affichage jusqu'à u_10
print("Termes jusqu'à u_10 :")
for i in range(11):
    print(f"u_{i} = {u(i)}")

# Affichage pour u_30 (attention, la récursion peut devenir lente si non optimisée)
print(f"u_30 = {u(30)}")

#3.
def calcul_suite(n):
    u = 1
    for i in range(n):
        u = (2 * u**2 + 1) / (u**2 + 1)
    return u

print(f"u_10 = {calcul_suite(10)}")
print(f"u_100 = {calcul_suite(100)}")
print(f"u_1000 = {calcul_suite(1000)}")
