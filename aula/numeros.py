def ParImpar(numero:float):
    if numero % 2 == 0:
        return "Par"
    if numero % 2 != 0:
        return "Impar"

def PositivoNegativoNeutro(numero:float):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Nulo"

def MaiorDaLista(lista:list):
    if not lista:
        return None
    
    maior_lista = lista[0]
    for i in lista:
        if i > maior_lista:
            maior_lista = i

    return maior_lista

def MenorDaLista(lista:list):
    if not lista:
        return None
    
    menor_lista = lista[0]
    for i in lista:
        if i < menor_lista:
            menor_lista = i

    return menor_lista

def MediaDaLista(lista:list):
    if not lista:
        return None
    soma_total = 0
    for i in lista:
        soma_total += i
    media = soma_total / len(lista)
    return media
