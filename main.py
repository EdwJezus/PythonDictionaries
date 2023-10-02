def dicionario():
    dicionario = {}
    with open('words.txt', 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                dicionario[word] = None
    return dicionario

# atividade 2 ############################
print('')

def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

# atividade 4 ############################
print('')

def has_duplicates(lst):
    d = {}
    for i in lst:
        if i in d:
            return True
        d[i] = True
    return False

# atividade 5 ############################

import string

def cesar(texto, deslocamento):
    alfabeto = string.ascii_lowercase
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    tabela = str.maketrans(alfabeto, alfabeto_deslocado)
    return texto.translate(tabela)

def encontrar_pares_rotacionados(palavras):
    dicionario = {}
    for palavra in palavras:
        for i in range(1, len(palavra)):
            rotacionado = cesar(palavra, i)
            if rotacionado in palavras:
                dicionario[palavra] = rotacionado
    return dicionario
