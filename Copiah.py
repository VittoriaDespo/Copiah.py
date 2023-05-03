
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(len(as_a)):
        soma = soma + (abs(as_a[i] - as_b[i]))
    S_ab = soma / 6
    return S_ab
    
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    soma_letras = 0
    car_sentenca = 0
    car_frases = 0
    palavras = [] 
    lista_frases = []
    for sent in sentencas:
        for caracteres in sent:
            car_sentenca = car_sentenca + 1
        novas_frases = separa_frases(sent)
        lista_frases.extend(novas_frases)
    for fr in lista_frases:
        for carac_frase in fr:
            car_frases = car_frases + 1
        novas_palavras = separa_palavras(fr)
        palavras.extend(novas_palavras)
    for pal in palavras:
        for let in pal:
            soma_letras = soma_letras + 1 
            
    palavras_dif = n_palavras_diferentes(palavras)
    palavras_un = n_palavras_unicas(palavras)

    wal = soma_letras / len(palavras)
    ttr = palavras_dif / len(palavras)
    hlr = palavras_un / len(palavras)
    sal = car_sentenca / len(sentencas)
    sac = len(lista_frases) / len(sentencas)
    pal = car_frases / len(lista_frases)
    
    return [wal,ttr,hlr,sal,sac,pal]
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    grau_simil = []
    for txt in textos:
        assinatura = calcula_assinatura(txt)
        compara = compara_assinatura(assinatura,ass_cp)
        grau_simil.append(compara)
    menor = grau_simil[0]
    index = 1
    for i in range(len(grau_simil)):
        if (menor > grau_simil[i]):
            index = i
    return index            
    
def main():
    assinatura = le_assinatura()
    textos = le_textos()
    index = avalia_textos(textos, assinatura)
    print("O autor do texto {} está infectado com COH-PIAH".format(index))
    
   
main()
    

    
    
    
    
 
    
    
    