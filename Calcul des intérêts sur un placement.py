# =====================================================================
# Étape commune : Saisie des données utilisateur
# =====================================================================
print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculés une fois par an.")

placement_depart = float(input("Entrer le placement de départ: "))
versement_mensuel = float(input("Entrer le montant du versement mensuel: "))
taux_annuel = float(input("Entrer le taux annuel en %: "))
annees = int(input("Entrer le nombre d'années: "))

taux_decimal = taux_annuel / 100

print("\n" + "=" * 70)
print(f" QUESTION 1 : Calcul des intérêts une fois par AN")
print("=" * 70)

# Initialisation pour le calcul annuel
capital_annuel = placement_depart
total_versements = placement_depart

# Boucle pour chaque année
for annee in range(1, annees + 1):
    # Ajout des 12 versements mensuels au cours de l'année
    capital_annuel += versement_mensuel * 12
    total_versements += versement_mensuel * 12

    # Calcul et application des intérêts une seule fois à la fin de l'année
    interets_annee = capital_annuel * taux_decimal
    capital_annuel += interets_annee

# Calcul des résultats demandés
interets_gagnes_annuel = capital_annuel - total_versements

# Affichage des résultats (strictement identique au format de l'image)
print(
    f"Le capital acquis avec intérêts est de {capital_annuel:.2f} euros au bout de {annees} ans avec des versements mensuels de {versement_mensuel:.0f} euros.")
print(f"Les intérêts gagnés au taux annuel de {taux_annuel:.1f} % sont de {interets_gagnes_annuel:.2f} euros.")
print(f"Sans placement avec intérêts le capital acquis serait de {total_versements:.0f} euros.")

print("\n" + "=" * 70)
print(f" QUESTION 2 : Calcul des intérêts une fois par MOIS")
print("=" * 70)

# Initialisation pour le calcul mensuel
capital_mensuel = placement_depart
taux_mensuel = taux_decimal / 12
nb_mois = annees * 12

# Boucle pour chaque mois
for mois in range(1, nb_mois + 1):
    # Le versement est fait en début/cours de mois
    capital_mensuel += versement_mensuel

    # Les intérêts sont calculés et ajoutés à la fin de chaque mois
    interets_mois = capital_mensuel * taux_mensuel
    capital_mensuel += interets_mois

interets_gagnes_mensuel = capital_mensuel - total_versements

print(f"Le capital acquis avec intérêts (calcul mensuel) est de {capital_mensuel:.2f} euros.")
print(f"Les intérêts gagnés sont de {interets_gagnes_mensuel:.2f} euros.")
print(f"Soit un gain supplémentaire de {capital_mensuel - capital_annuel:.2f} euros dû aux intérêts composés mensuels.")