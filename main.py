
"""Module d'encodage ASCII art avec algorithmes itératif et récursif."""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif.
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    l = []
    count = 1
    current_car = s[0]
    for car in s[1:]:
        if car == current_car:
            count += 1
        else:
            l.append((current_car, count))
            current_car = car
            count = 1
    l.append((current_car, count))
    return l

def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif.
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [(s[0], 1)]
    rest = artcode_r(s[1:])
    if s[0] == rest[0][0]:
        return [(s[0], rest[0][1] + 1)] + rest[1:]
    return [(s[0], 1)] + rest

#### Fonction principale


def main():
    """Fonction principale pour tester les algorithmes d'encodage."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
