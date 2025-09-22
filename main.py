#### Fonction secondaire

def alphanumerical(s):
    """
    supprime les espaces et caractères spéciaux et convertit les accents d'une chaine entrée en paramètres

    Args:
        s: string quelqconque

    Returns:
        alphanumerical("pp6 5 é-'-àçk oq 6") : "pp65eackoq6"
    """
    alphaNumString = []
    dict_caracteres_speciaux = {
        "à" : "a",
        "ä" : "a",
        "â" : "a",
        "ç" : "c",
        "é" : "e",
        "è" : "e",
        "ë" : "e",
        "ê" : "e",
        "ï" : "i",
        "ô" : "o",
        "ù" : "u",
        "ü" : "u",
        "û" : "u",
        " " : "",
        "-" : "",
        "," : "",
        "'" : "",
        "?" : "",
        "!" : "",
        "." : "",
        ":" : ""
    }
    s = s.lower()
    for cle,valeur in dict_caracteres_speciaux.items():
        s = s.replace(cle,valeur)
    return s


def ispalindrome(p):
    """
    retourne vrai si la chaine de caractères en paramètre est un palindrone, et faux sinon

    Args:
        s: string quelqconque

    Returns:
        ispalindrome("kayak") : True
        ispalindrome("pelle") : False
    >>> ispalindrome("radar")
    True
    >>> ispalindrome("0")
    True
    >>> ispalindrome("1221")
    True
    >>> ispalindrome("civique")
    False
    >>> ispalindrome("52")
    False
    """
    chaine = alphanumerical(p)
    for i in range (0,len(chaine)):
        if chaine[i] != chaine[-i-1]:
            return False
    return True

#### Fonction principale

def main():
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
