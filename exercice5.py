a = 0.5  # Valeur de a_1
print(f"a_1 = {a}")

for n in range(2, 11):
    a = 0.5 * a + 0.3
    print(f"a_{n} = {a:.5f}")