#1.
n=int(input("Entrer n: "))
s=0
for i in range(n+1):
    s=s+i
    print("i= ",i, " - s= ",s)
#Ce programme calcule et affiche pas à pas la somme des entiers consécutifs de $0$ jusqu'à $n$.

#2.
n = int(input("Entrer n : "))

# Initialisation des trois sommes
S = 0
T = 0
U = 0

for i in range(1, n + 1):
    # Somme S : 1/1 + 1/2 + 1/3 + ... + 1/n
    S += 1 / i

    # Somme T : 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/n^2
    T += 1 / (i ** 2)

    # Somme U : 1 + 1/2^1 + 1/2^2 + ... + 1/2^(n-1)
    U += 1 / (2 ** (i - 1))

# Affichage des résultats
print(f"\nPour n = {n} :")
print(f"S = {S:.6f}")
print(f"T = {T:.6f}")
print(f"U = {U:.6f}")

#3.
#La suite S diverge vers + inf; la suite T converge vers un limite de 1?64 et la suite U converge vers 2