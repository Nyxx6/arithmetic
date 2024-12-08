import numpy as np 
from fractions import Fraction
import matplotlib.pyplot as plt
# Predefined list of prime numbersthe rules of attraction
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
          73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
          157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
          239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
          331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
          421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
          509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
          613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
          709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
          821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
          919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

def bezout_identity(a, b):
    # Initialize variables for Bézout coefficients
    u = 0; old_u = 1
    v = 1; old_v = 0
    # Initialize variables for remainder
    r = b; old_r = a

    # Iterate until the remainder becomes zero
    while r != 0:
        # Calculate quotient and update remainder
        q = old_r // r
        old_r, r = r, old_r - q * r
        # Update Bézout coefficients
        old_u, u = u, old_u - q * u
        old_v, v = v, old_v - q * v

    # Return a list containing the GCD and Bézout coefficients
    return [old_r, old_u, old_v]

# Function to find positive divisors and Euler indicator of a number
def positive_divisors_and_euler_indicator(n):
    # Generate a list of divisors
    divisors = [i for i in range(1, n // 2 + 1) if n % i == 0]
    divisors.append(n)  # Include n as a divisor
    
    euler_indicator = n  # Initialize result with n
    decomp = list(set(decomposition_nombres_premiers(n)))  # Decompose the number into prime factors
    
    # Iterate over prime factors and update Euler indicator
    for prime in decomp:
        euler_indicator *= (1 - Fraction(1, prime))
    
    return divisors, euler_indicator

# Function to decompose a number into prime factors
def decomposition_nombres_premiers(n):
    facteurs = []  # List to store prime factors
    for prime in PRIMES:  # Iterate over precomputed list of prime numbers
        if prime > n // 2:
            break
        while n % prime == 0:
            n //= prime
            facteurs.append(prime)  # Add prime factor to the list
    if n > 1:
        facteurs.append(n)  # If there is a remaining factor, add it to the list
    return facteurs

def uniforme():
    uniform_random = np.random.uniform(0, 1, 100)
    return uniform_random

def exponential(n, lam):
    # Generer la séquence U avec la loi uniforme
    U = np.random.uniform(0, 1, n)
    print(f"Données générer avec la loi uniforme: {U}")

    # F^−1(U) = -ln(1 - U) / λ Echantillonnage inverse pour trouver x
    X = -np.log(1 - U) / lam
    print(f"Données échantillonnées: {X}")
    return X

def poisson(lam, n):
    poisson_random = np.random.poisson(lam, n)
    return poisson_random

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
# Checking only odd numbers
# Iterating in steps of 2, starting from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def menu():
    print("\n")
    print("1. Uniform Random Number")
    print("2. Exponential Random Number")
    print("3. Poisson Random Number")
    choice = input("Entrer le nombre de votre choix: ")

    if choice == '1':
        uniform_random = uniforme()
        print(f"Loi uniforme: {uniform_random}")
    elif choice == '2':
        # Parametres de la fonction de distribution exponentielle
        lam = 0.5  # le taux lambda
        nbr_echant = 10 # taille de la sequence de nbr aleatoires à generer
        # Appel à la fonction de distribution exponentielle
        X = exponential(nbr_echant, lam)
        # f (x) =λe(−λx) Calcule de la densité
        fd = lam * np.exp(-lam * X)
        print(f'Densité de Probabilité: {fd}')
    elif choice == '3':
        lam = 40
        n = 3
        poisson_random = poisson(lam, n)
        print(f"Loi de poisson: {poisson_random}")
    else:
        print("Choix Invalide.")
"""
Exemple, si un événement se produit en moyenne 4 fois par minute, pour étudier le nombre d'événements se produisant dans un laps de temps de 10 minutes, on choisit comme modèle une loi de Poisson de paramètre λ = 10×4 = 40.
"""
def main():
    while True:
        print("\nMenu:")
        print("0. TP0: Positive Prime number")
        print("1. TP1: Euclidean Algorithm (PGCD)")
        print("2. TP2: Bezout Identity")
        print("3. TP3: Positive Divisors and Euler Indicator")
        print("4. TP4: Generate Random Numbers")
        print("5. Exit")

        choice = input("Enter your choice (0-5): ")
        if choice == "0":
            n = int(input("Enter an integer (n): "))
            if(is_prime(n)) : print(f"{n} is a prime number.")
            else : print(f"{n} is not a prime number.")

        elif choice == "1":
            a = int(input("Enter the first integer (a): "))
            b = int(input("Enter the second integer (b): "))
            print(f"PGCD of {a} and {b} is: {euclidean_algorithm(a, b)}")

        elif choice == "2":
            a = int(input("Enter the first integer (a): "))
            b = int(input("Enter the second integer (b): "))
            gcd, u, v = bezout_identity(a, b)
            print(f"GCD of {a} and {b} is: {gcd}")
            print(f"Coefficients (u, v) for Bezout Identity: ({u}, {v})")

        elif choice == "3":
            n = int(input("Enter the integer (n): "))
            divisors, euler_indicator = positive_divisors_and_euler_indicator(n)
            print(f"Positive divisors of {n}: {divisors}")
            print(f"Euler Indicator of {n}: {euler_indicator}")

        elif choice == "4":
            menu()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
