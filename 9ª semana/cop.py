import re


def tam_medio_pal(texto):
    soma=0
    palavras=[]
    palavras=separa_palavras(texto)
    qnt=len(palavras)
    for i in palavras:
        soma=soma+len(i)
    media=soma/qnt
    return media

def type_token(texto):
    lista=separa_palavras(texto)
    total=len(lista)
    qnt_diferente=n_palavras_diferentes(lista)
    typeToken=qnt_diferente/total
    return typeToken

def hapax_legomana(texto):
    lista=separa_palavras(texto)
    total=len(lista)
    qnt_unica=n_palavras_unicas(lista)
    hapaxLeg=qnt_unica/total
    return hapaxLeg

def media_frases_sent(sentencas):#REFAZER
    soma=0
    for i in sentencas:
        soma+=len(separa_frases(sentenca[i]))
    return soma/len(sentencas)


def complexidade_sentença(texto):
    n_sentencas=len(separa_sentencas(texto))
    n_frases=len(separa_frases(texto))
    res=n_frases/n_sentencas
    return res

def media_carac_frases(frases):#REFAZER
    soma=0
    for i in frases:
        soma+=len(frases[i])
    return soma/len(frases)







def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
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
    s=((as_a[0]-as_b[0])+(as_a[1]-as_b[1])+(as_a[2]-as_b[2])+(as_a[3]-as_b[3])+(as_a[4]-as_b[4])+(as_a[5]-as_b[5]))/6
    return s

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal=tam_medio_pal(texto)
    ttr=type_token(texto)
    hlr=hapax_legomana(texto)
    sal=media_frases_sent
    sac=complexidade_sentença
    pal=media_carac_frases
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas=[]
    for i in textos:
        assinaturas.append(calcula_assinatura(textos[i]))
        i+=1

    valor=[]
    for i in assinaturas:
        valor=compara_assinatura(assinaturas[i],ass_cp)
    i=0
    posicao=0
    menor=valor[j]
    tam=len(valor)
    while i<tam:
        if(valor[i]<menor):
            menor=valor[i]
            posicao=i
        i+=1
    return posicao

    
def main():
    assinatura=le_assinatura()
    textos=le_textos()
    copia=avalia_textos(textos,assinatura)
    print("O autor do texto ", (copia+1), " está infectado com COH-PIAH")
    

main()