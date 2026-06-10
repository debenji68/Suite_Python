#1.
#a.
def evolution_population():
    pop = 2000
    annee_initiale = 2000

    # On simule l'évolution sur 26 ans (jusqu'en 2026)
    for i in range(1, 27):
        pop = pop * 1.03
        annee = annee_initiale + i

        # Affichage ciblé pour les années demandées
        if annee in [2001, 2002, 2010, 2026]:
            print(f"Population en {annee} : {pop:.2f} habitants (soit environ {round(pop)})")


evolution_population()

#b.
pop = 2000
annee = 2000

while pop < 6000:
    pop = pop * 1.03
    annee += 1

print(f"La population aura triplé (>= 6000) en l'année : {annee} (Population : {pop:.2f})")

#2.
#a.
import matplotlib.pyplot as plt


def simulation_flux_simple(annees=50):
    # Conditions initiales
    A = 50000
    B = 2000

    # Listes pour stocker l'historique des données graphiques
    historique_A = [A]
    historique_B = [B]
    historique_annees = [0]

    for annee in range(1, annees + 1):
        # Calcul des nouveaux flux (attention à utiliser des variables temporaires)
        nouveau_A = 0.90 * A + 0.30 * B
        nouveau_B = 0.10 * A + 0.70 * B

        # Mise à jour des populations
        A = nouveau_A
        B = nouveau_B

        # Sauvegarde pour le graphique
        historique_A.append(A)
        historique_B.append(B)
        historique_annees.append(annee)

    # Création du graphique
    plt.figure(figsize=(10, 5))
    plt.plot(historique_annees, historique_A, color='red', label='Ville A')
    plt.plot(historique_annees, historique_B, color='blue', label='Village B')
    plt.title("Évolution des populations entre la ville A et le village B (Flux simples)")
    plt.xlabel("Années écoulées")
    plt.ylabel("Nombre d'habitants")
    plt.legend()
    plt.grid(True)
    plt.show()

# Appeler la fonction pour afficher le graphique
# simulation_flux_simple()

#b.
def simulation_flux_avec_fuite(annees=50):
    A = 50000
    B = 2000

    historique_A = [A]
    historique_B = [B]
    historique_annees = [0]

    for annee in range(1, annees + 1):
        # 10% de A vont en B, 30% de B vont en A
        # De plus, 5% de B partent définitivement (B ne garde que 100% - 30% - 5% = 65%)
        nouveau_A = 0.90 * A + 0.30 * B
        nouveau_B = 0.10 * A + 0.65 * B

        A = nouveau_A
        B = nouveau_B

        historique_A.append(A)
        historique_B.append(B)
        historique_annees.append(annee)

    # Création du graphique
    plt.figure(figsize=(10, 5))
    plt.plot(historique_annees, historique_A, color='red', linestyle='--', label='Ville A (avec fuite de B)')
    plt.plot(historique_annees, historique_B, color='blue', linestyle='--', label='Village B (avec fuite de B)')
    plt.title("Évolution des populations (5% de B quittent le système chaque année)")
    plt.xlabel("Années écoulées")
    plt.ylabel("Nombre d'habitants")
    plt.legend()
    plt.grid(True)
    plt.show()

# Appeler la fonction pour afficher le graphique
# simulation_flux_avec_fuite()