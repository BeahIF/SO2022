from ast import Delete
from random import sample
import random
from alternancia import alternanciaCircular
from prioridades import prioridades
import logging
import threading
import time
def loteria(linhas):
    print("no loterias")
    clok = linhas[0].split("|")
    clok = clok[1]
    linhas.pop(0)
    somabilhetes = 0
    finalzados=[]
    processos = []
    processos2=[]
    ordena = {}
    cont=0
    for n in linhas:
        quebra = n.split('|')
        processos.append(quebra)
        somabilhetes = somabilhetes + int(quebra[3])
    sorteados = sample(range(0, somabilhetes), somabilhetes)
    for n in processos:
        i=0  
        vetbilhetes=[]
        while (i< int(n[3])):

            vetbilhetes.append(sorteados[cont])
            i += 1
            cont += 1
       
        n.append(vetbilhetes)
        n.append(0)
        processos2.append(n)
    while (len(processos2)>0):
        random.shuffle(sorteados)
        print(sorteados[0])
        for n in processos2:
            try:
                tem = n[6].index(sorteados[0])
            except:
                tem = -1
            if tem > -1:
                diminuiTempo = int(n[2])-int(clok)
                #copia = str(n[0])+"|"+str(n[1])+"|"+str(diminuiTempo)+"|"+str(n[3])+"|"+str(n[4])+"|"+str(n[5])+"|"+str(n[6])+"|"+str(int(n[7])+1) 
                
                if(int(diminuiTempo)>0):
                    n[2] = str(diminuiTempo)
                    n[7] = int(n[7]) + 1
                else:
                    processos2.remove(n)
                    sorteados = retirasorteados(sorteados,n[6])
                #    linhas.append(copia)
                if(diminuiTempo==0):
                    finalzados.append("O processo "+str(n[0])+" demorou "+str(n[7])+" para terminar.")
                else:
                    print("Na CPU:"+str(n[0])+" faltam "+str(diminuiTempo)+" para concluir o processo.")
                    # print("Na CPU:"+str(n[0])+" faltam "+str(diminuiTempo)+" para concluir o processo.")
def retirasorteados(sorteados, vet):
    for i in vet:
        try:
            tem = sorteados.index(i)
        except:
            tem = -1
        if tem > -1:
            del(sorteados[tem])
    return(sorteados)

    
        