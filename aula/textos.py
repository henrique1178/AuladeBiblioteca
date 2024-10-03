def QtdDeVogais(palavra:str):
    vogal = "aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãẽĩõũÃẼĨÕŨâêîôûÂÊÎÔÛ"
    contador = 0

    for letra in palavra:
        if letra in vogal:
            contador += 1
    return contador

def QtdDeConsoantes(palavra:str):
    consoantes = "qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZCXVBNM"
    contador = 0

    for letra in palavra:
        if letra in consoantes:
            contador += 1
    return contador

def QtdDePalavras(frase:str):
    espaços = " "
    contador = 1

    for letra in frase:
        if letra in espaços:
            contador += 1
    return contador

def PalavraMaiusculo(palavra:str):
    return palavra.upper()

def PalavraMinusculo(palavra:str):
    return palavra.lower()