#menor o numero, maior a prioridade
import heapq as hq 

def prioridades(linhas,tempo):
    newDict = {}
    # print(len(linhas))
    for i in linhas:
        original =  i.split("|")
        newDict[original[0]] = int(original[3])
        # newDict.append({int(original[3]):original[0]})
        # , original[1], original[2], original[4], original[5], original[6])) 
    # print(len(newDict))
    # print(newDict)
    ordena = {}
    for i in sorted(newDict, key = newDict.get):
        ordena[i]= newDict[i]
    finalizados = []
    print("iniciando o processo")
    # print(ordena)
    while(len(linhas)>0):
        print(len(linhas))

    #     hq.heapify(ordena)  
    #     # ordem como ficou: 0 -> prioridade 1-> nome
    # # 2 -> tempoDeExecução 3 -> prioridade
    # # 4 -> UID 5-> qtdeMemoria
    # # salvar em ordem quanto demorou cada processo
    # # retirar sem fazer o append
    #     print(ordena[0][0],':',ordena[0][1])  

        for i in ordena:
            print(i)
            linha= encontra(i, linhas)
            print(linha)
            if(linha == None):
                del ordena[i]
            else:
                original =  linha.split("|")
        #         print(i[0],':',i[1],':',i[3])  

                diminuiTempo = int(original[2])-int(tempo)
                copia = str(original[0])+"|"+str(original[1])+"|"+str(diminuiTempo)+"|"+str(original[3])+"|"+str(original[4])+"|"+str(original[5])+"|"+str(int(original[6])+1) 

                if(int(diminuiTempo)>0):
                    linhas.append(copia)
                if(diminuiTempo==0):
                    print("O processo "+str(original[0])+" demorou "+str(original[6])+" para terminar.")
                else:
                    finalizados.append("Na CPU:"+str(original[0])+" faltam "+str(diminuiTempo)+" para concluir o processo.")
                    # print("Na CPU:"+str(original[0])+" faltam "+str(diminuiTempo)+" para concluir o processo.")
                linhas.remove(linha)
    #             # index= index+1
    #         hq.heapify(ordena)  

    # print(ordena)
def encontra(processoName, linhas):
    for i in linhas:
        
        original =  i.split("|")
        if(original[0] == processoName):
            return i