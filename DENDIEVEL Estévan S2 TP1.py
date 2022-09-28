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
    1while 
    >>> deux_puissance(1)
    2
    >>> deux_puissance(2)
    4
    '''

    return 2**rang


### Q4

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
    while i < len(binaire):
        binaire[i] 
        i=i+1

    return reponse

### --- Exercice 2 --- ###









if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
