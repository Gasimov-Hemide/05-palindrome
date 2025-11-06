#### Fonction secondaire
"""
Vérifie si une chaîne de caractère est un palindrome

Modules:
    ispalindrome(p)
    main()
"""
def ispalindrome(p):
    """
    Vérifie si une chaîne de caractère p est un palindrome 

    Arguments:
        p: une chaîne de caractère
        a: une chaîne de caractère

    Retours:
        palindrome: un booléan, vrai si la chaîne de caractère est un palindrome
    """
    # votre code ici
    p = p.lower().translate(str.maketrans('éèêëàâäîïôöùûüç','eeeeaaaiioouuuc',' -.,?!;:/\''))
    a = p[::-1]

    palindrome = True
    l=len(p)
    for i in range(l):
        if p[i-1] != a[i-1]:
            palindrome = False
            break
    return palindrome

#### Fonction principale

def main():
    """
    Fait des appels de test grâce au module ispalindrome
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
