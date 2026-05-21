from pylab import *
def u(n):
    return n**2-3

for n in range(10):
    print(u(n))

#1. Le programme affiche -3; -2; 1; 6; 13; 22; 33; 46; 61; 78

#3.
def u(n):
    return (2 * n**2 - 1) / (n**2 + 2)
for n in range(100):
    print(u(n))
    plot(n, u(n), '*b')
show()

#4.
def u(n):
    return (2 * n**2 - 1) / (n**2 + 2)

compteur = 0
for n in range(0, 100, 3):
    print(f"u({n}) = {u(n)}")
    plot(n, u(n), '*b')
    compteur += 1  # On incrémente le compteur à chaque passage

print("Nombre de termes affichés :", compteur)
show()