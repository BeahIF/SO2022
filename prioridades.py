#menor o numero, maior a prioridade
import heapq as hq 

def prioridades(linhas,tempo):
    newDict = {}
    for i in linhas:
        original =  i.split("|")
        newDict[original[0]] = int(original[3])
 
    ordena = {}
    for i in sorted(newDict, key = newDict.get):
        ordena[i]= newDict[i]
    finalizados = []
    print("iniciando o processo")
    
    while(len(linhas)>0):

        for i in ordena.copy():
            linha= encontra(i, linhas)
            if(linha == None):
                del ordena[i]
            else:
                original =  linha.split("|")
                diminuiTempo = int(original[2])-int(tempo)
                copia = str(original[0])+"|"+str(original[1])+"|"+str(diminuiTempo)+"|"+str(original[3])+"|"+str(original[4])+"|"+str(original[5])+"|"+str(int(original[6])+1) 
                if(int(diminuiTempo)>0):
                    linhas.append(copia)
                if(diminuiTempo==0):
                    finalizados.append("O processo "+str(original[0])+" demorou "+str(original[6])+" para terminar.")
                else:
                    print("Na CPU:"+str(original[0])+" faltam "+str(diminuiTempo)+" para concluir o processo.")
                linhas.remove(linha)
    for i in finalizados:
        print(i)
def encontra(processoName, linhas):
    for i in linhas:
        
        original =  i.split("|")
        if(original[0] == processoName):
            return i