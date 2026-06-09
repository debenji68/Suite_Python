#1 : un = n**2 − n + 1
#a. Déterminer la limite de cette suite. --> lim = + inf
#b. Déterminer le rang n0 à partir duquel on a, pour tout n ≥ n0, un≥1000 -->  Le premier entier naturel qui vérifie cette condition est donc $n_0 = 33$.

def u(n):
    return n**2-n+1

n=0
while u(n)<1000:
    print(u(n))
    n=n+1

print(n)
# À chaque itération, il affiche la valeur du terme $u_n$ tant que celle-ci est strictement inférieure à 1000. Il va donc lister toutes les valeurs de la suite de $u_0$ jusqu'à $u_{32}$ (car $u_{32} = 32^2 - 32 + 1 = 993 < 1000$).
def u(n):
    return (2 * n**2 - 1) / (n**2 + 2)

n = 0
while u(n) <= 1.999:
    n += 1

print(f"Le rang recherché est n = {n}")