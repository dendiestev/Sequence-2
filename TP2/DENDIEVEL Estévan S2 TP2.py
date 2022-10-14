### --- Exercice 1 --- ###


### Q1


def valeur_absolue(nombre:int) -> int :
    '''
    >>> valeur_absolue(7)
    7
    >>> valeur_absolue(-6)
    6
    '''
    if nombre < 0:
        nombre = -nombre
    print(nombre)


### Q2

def inverse(binaire:str) -> str :
    '''
    >>> inverse("1010")
    '0101'
    >>> inverse("10110011")
    '01001100'
    '''
    i=0
    rep = ''
    while len(binaire) > i:
        if binaire[i] == '0':
            rep = rep + '1'
        else:
            rep = rep + '0'
        i=i+1
    return rep


### Q3


def addition_binaire(nombre1:str, nombre2:str) -> str :
    '''
    >>> addition_binaire('1001','0001')
    '1010'
    >>> addition_binaire('0001','0001')
    '0010'
    >>> addition_binaire('1010','0101')
    '1111'
    '''
    nbplusgrand = 0
    resultat = ''
    result1 = 0
    retenue = '0'
    if len(nombre1) < len(nombre2):
        nbplusgrand = len(nombre2)
    else:
        nbplusgrand = len(nombre1)
    i=0
    while i < nbplusgrand:
        result1 = (nbplusgrand-i)-1
        ## Si nombre 1 == 1
        if nombre1[result1] == '1':
            ## Si nombre 1 == 1 & nombre 2 == 0
            if nombre2[result1] == '0':
                ## On vérifie la retenue
                if retenue == '0':
                    resultat = '1'+resultat
                    retenue = '0'
                else:
                    resultat = '0'+resultat
                    retenue = '1'
            ## Si nombre 1 == 1 & nombre 2 == 1
            else:
                ## On vérifie la retenue
                if retenue == '0':
                    resultat = '0'+resultat
                    retenue = '1'
                else:
                    resultat = '1'+resultat
                    retenue = '1'
        if nombre2[result1] == '1':
            if nombre1[result1] == '0':
                if retenue == '0':
                    resultat = '1'+resultat
                    retenue = '0'
                else:
                    resultat = '0'+resultat
                    retenue = '1'
        if nombre2[result1] == '0' and nombre1[result1] == '0':
            if retenue == '0':
                resultat = '0'+resultat
                retenue = '0'
            else:
                resultat = '1'+resultat
                retenue = '0'
        i=i+1
    return(resultat)

### --- Exercice 2 --- ###

## Q1 

def complement_a_deux(nombre:int, nb_bits:int) -> str :
    '''
    >>> complement_a_deux(-12, 8)
    '11110100'
    >>>> complement_a_deux(7,8)
    '00000111'
    '''






if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
