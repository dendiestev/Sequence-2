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
    '''
    nbplusgrand = 0
    resultat = ''
    retenue = 0
    if len(nombre1) < len(nombre2):
        nbplusgrand = len(nombre2)
    else:
        nbplusgrand = len(nombre1)
    i=0
    while i < nbplusgrand:
        ##if nombre1[i] and nombre2[i] == '1' or nombre1[i] and retenue == '1' or nombre2[i] and retenue == '1':
        if nombre1[i] == '1' and nombre2[i] == '1':
            retenue = 1
            resultat = '0'+resultat
        elif nombre1[i] == '1' and retenue == '1':
            retenue = 1
            resultat = '0'+resultat
        elif retenue == '1' and nombre2[i] == '1':
            retenue = 1
            resultat = '0'+resultat
        else:
            result1 = int(nombre1[i])+int(nombre2[i])
            result1 = str(result1)
            resultat = result1+resultat

            ###resultat = (nombre1[i]+nombre2[i])+resultat
        i=i+1
    return(resultat)




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
