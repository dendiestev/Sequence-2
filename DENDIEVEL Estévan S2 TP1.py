### --- Exercice 1 --- ###


### Q1

def est_valide(binaire:str) -> bool:
    '''
    >>> est_valide("100010101")
    True
    >>> est_valide("1010401034")
    False
    '''
    i=0
    reponse = True
    while i < len(binaire):
        if binaire[i] == "0" or binaire[i] == "1":
            reponse = True
        else: reponse = False
        i=i+1
    return reponse

### Q2

def est_pair(binaire:str) -> bool:
    '''
    >>> est_pair('1001')
    False
    >>> est_pair('1010')
    True
    '''

    reponse = True
    binaire = int(binaire)
    for i in range(1, binaire + 1):
        if i % 2 == 0:
            reponse = True
        else: reponse = False
    return reponse


### Q3

def deux_puissance(rang:int) -> int:
    '''
    >>> deux_puissance(0)
    1
    >>> deux_puissance(1)
    2
    >>> deux_puissance(2)
    4
    '''
    resultat = 1

    for _ in range(1,rang+1):
        resultat = resultat*2
    return resultat

    

### Q4



def inverse(mot:str) -> str:
    nouveau_mot = ""
    for indice in range(len(mot)-1,-1,-1):
        nouveau_mot = nouveau_mot+mot[indice]
    return nouveau_mot




def binaire_en_decimal(binaire:str) -> int:
    '''
    >>> binaire_en_decimal("1")
    1
    >>> binaire_en_decimal("1010")
    10
    >>> binaire_en_decimal("1001")
    9
    '''

    reponse = 0
    i=0
    chaine_cr = inverse(binaire)
    
    while i < len(binaire):
        ##binaire = int(binaire)
        if chaine_cr[i] == "1":
            reponse = 2**i+reponse
        i=i+1

    return reponse





### --- Exercice 2 --- ###


### Q1

def division_euclidienne(nombre:int, diviseur:int) -> tuple :
    '''
    >>> division_euclidienne(6, 3)
    (2, 0)
    >>> division_euclidienne(10, 4)
    (2, 2)
    >>> division_euclidienne(6, 0)
    None
    '''
    multiplicateur = nombre  // diviseur
    reste = nombre % diviseur
    return (multiplicateur,reste)





if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
