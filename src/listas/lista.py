# Busca linear em lista em alocação sequencial

def busca(lista, elem):
    """
    Retorna o índice do elem se ele estiver na lista ou None, caso contrário
    O(n)
    """
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None


lista = [10, 15, "5", 0, 32, "python", 11]
elemento = 32

indice = busca(lista, elemento)

if indice is not None:
    print("O índice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não está presente na lista".format(elemento))
