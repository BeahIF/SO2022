
# ordem : 0 -> nomeProcesso 1-> PID
# 2 -> tempoDeExecução 3 -> prioridade
# 4 -> UID 5-> qtdeMemoria
# salvar em ordem quanto demorou cada processo
# retirar sem fazer o append
def alternanciaCircular(linhas, tempo):
    
    index = 1
    
    while(len(linhas)>0):
        print("iniciando o processo")
        
        for i in linhas:
            original =  i.split("|")
            diminuiTempo = int(original[2])-int(tempo)
            copia = str(original[0])+"|"+str(original[1])+"|"+str(diminuiTempo)+"|"+str(original[3])+"|"+str(original[4])+"|"+str(original[5])+"|"+str(int(original[6])+1) 
            if(int(diminuiTempo)>0):
                linhas.append(copia)
            if(diminuiTempo==0):
                print("O processo "+str(original[0])+" demorou "+str(original[6])+" para terminar.")
            else:
                print("Na CPU:"+str(original[0])+" faltam "+str(diminuiTempo)+" para concluir o processo.")
            linhas.remove(i)
            index= index+1
