def u(n):
    return 3*n-2

print(u(2))

n=10
print(u(n))

#1. Le programme affiche 4 et 28
#2.
def v(n):
    return (2*(n**2)-1)/((n**2)+2)

print(v(10))
print(v(100))
print(v(1000))

# On observe que pour des valeurs de $n$ de plus en plus grandes, les termes de la suite se rapprochent de plus en plus de 2. On peut conjecturer que la limite de la suite est 2.