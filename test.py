import numpy as np

def exponential(n, lam):
    # Generer la séquence U avec la loi uniforme
    U = np.random.uniform(0, 1, n)
    print(f"Données générer avec la loi uniforme: {U}")

    # F^−1(U) = -ln(1 - U) / λ Echantillonnage inverse pour trouver x
    X = -np.log(1 - U) / lam
    print(f"Données échantillonnées: {X}")
    
    return X

# Parametres de la fonction de distribution exponentielle
lam = 0.5  # le taux lambda
nbr_echant = 10 # taille de la sequence de nbr aleatoires à generer

# Appel à la fonction de distribution exponentielle
X = exponential(nbr_echant, lam)


# f (x) =λe(−λx) Calcule de la densité
fd = lam * np.exp(-lam * X)

print(f'Densité de Probabilité: {fd}')

