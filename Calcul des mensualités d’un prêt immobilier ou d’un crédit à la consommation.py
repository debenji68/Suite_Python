print("Calcul d'un prêt immobilier ou d'un crédit à la consommation.")

# 1. Saisie des données par l'utilisateur
capital_initial = float(input("Entrer le montant du prêt ou crédit: "))
taux_annuel = float(input("Entrer le taux annuel en %: "))
annees = int(input("Entrer le nombre d'années: "))

# 2. Calculs préliminaires
nb_mois = annees * 12
taux_mensuel = (taux_annuel / 100) / 12

# Formule de la mensualité constante en utilisant l'opérateur de puissance **
mensualite = capital_initial * (taux_mensuel / (1 - (1 + taux_mensuel) ** -nb_mois))

# Calcul du total des intérêts
total_interets = (mensualite * nb_mois) - capital_initial

print(f"La mensualité avec intérêts est de {mensualite:.2f} euros")
print(f"Le montant des intérêts remboursés sont de {total_interets:.2f} euros.")
print(f"Le taux mensuel est de {taux_mensuel:.4f}\n")

# 3. Affichage du tableau d'amortissement
print("Tableau d'amortissement:")
print("Mois - Mensualité - Intérêts - Capital remboursé - Capital restant du - Intérêts remboursés")

capital_restant = capital_initial
cumul_interets = 0.0

for mois in range(1, nb_mois + 1):
    # Calcul des intérêts du mois sur le capital restant dû
    interets_mois = capital_restant * taux_mensuel

    # Le capital remboursé ce mois-ci
    capital_rembourse_mois = mensualite - interets_mois

    # Mise à jour du capital restant dû
    capital_restant -= capital_rembourse_mois

    # Cumul des intérêts remboursés
    cumul_interets += interets_mois

    # Sécurité pour le dernier mois (gestion des arrondis des nombres à virgule)
    if capital_restant < 0 or mois == nb_mois:
        capital_rembourse_mois += capital_restant
        capital_restant = 0.0

    # Affichage de la ligne formatée
    print(
        f" {mois:<3} -  {mensualite:.1f}   -   {interets_mois:.1f}  -      {capital_rembourse_mois:.1f}     -     {capital_restant:.1f}     -   {cumul_interets:.2f}")