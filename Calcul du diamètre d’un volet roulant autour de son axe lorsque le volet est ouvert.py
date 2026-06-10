import math


def simulation_volet_roulant():
    print("--- APPLICATION NUMÉRIQUE : ENROULEMENT DU VOLET ---")

    # 1. Entrées utilisateur (comme sur la capture d'écran de la console)
    diametre_axe = float(input("Entrer le diamètre de l'axe en mm: "))
    nb_tours = int(input("Entrer nombre de tours n: "))

    # Paramètres de l'énoncé
    epaisseur_lame = 7.5  # mm
    augmentation_tour = 1.5  # mm

    # Raison de la suite arithmétique du diamètre
    # À chaque tour, le diamètre augmente de : 2 * (épaisseur + jeu de rigidité)
    raison = 2 * (epaisseur_lame + augmentation_tour)  # 18.0 mm

    print("\nCalcul de la longueur L pour chaque tour:")

    longueur_cumulee = 0

    # 2. Méthode itérative : Tour par tour
    for tour in range(1, nb_tours + 1):
        # Équation de la suite du diamètre : d_n = d_0 + r * n
        diametre_actuel = diametre_axe + (raison * tour)

        # Circonférence du tour actuel : c_n = pi * d_n
        circonference_tour = math.pi * diametre_actuel

        # Cumul de la longueur du tablier enroulé
        longueur_cumulee += circonference_tour

        print(
            f"Tour: {tour:<2d} - Diamètre [mm]: {diametre_actuel:.1f} - Longueur enroulée [mm]: {round(longueur_cumulee)}")

    # 3. Méthode directe : Utilisation de la formule de la somme
    # Somme d'une suite arithmétique appliquée à la circonférence :
    # L_n = pi * [ (n * d_0) + r * (n * (n + 1) / 2) ]
    longueur_formule = math.pi * ((nb_tours * diametre_axe) + raison * (nb_tours * (nb_tours + 1) / 2))

    print("\nCalcul de la longueur L par formule:")
    print(f"Longueur [mm] pour {nb_tours} tours: {longueur_formule}")


# Exécution du script
if __name__ == "__main__":
    simulation_volet_roulant()