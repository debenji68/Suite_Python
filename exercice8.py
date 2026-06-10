#1.
adherents = 500
mois = 24

print("Évolution du nombre d'adhérents :")
print(f"Mois 0 : {adherents} adhérents")

for m in range(1, mois + 1):
    # -5% d'adhérents + 30 nouveaux
    adherents = 0.95 * adherents + 30
    print(f"Mois {m} : {adherents:.2f} adhérents (arrondi à {round(adherents)})")

#2.
adherents = 500
prix_adhesion = 10
total_cotisations = 0

for m in range(1, 25):
    adherents = 0.95 * adherents + 30
    # On ajoute les cotisations perçues ce mois-ci
    total_cotisations += adherents * prix_adhesion

print(f"Le montant total des cotisations perçues en 2 ans est de : {total_cotisations:.2f} €")

#3.
# Calcul du nombre cumulé de mensualités d'adhérents sur 24 mois
adherents = 500
total_mensualites = 0

for m in range(1, 25):
    adherents = 0.95 * adherents + 30
    total_mensualites += adherents

# Scénario B : Financer le fonctionnement courant + la structure de 20 000€
budget_total_necessaire = (total_mensualites * 10) + 20000
nouveau_prix = budget_total_necessaire / total_mensualites

print(f"Le montant de l'adhésion mensuelle devrait être de : {nouveau_prix:.2f} €")