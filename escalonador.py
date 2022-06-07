import random
from alternancia import alternanciaCircular
from loteria import loteria
from prioridades import prioridades

def main():
    linhas =[] 
    with open("alternancia.txt", "r") as tf:
        lines = tf.read().split('\n')        
    for line in lines:
        linhas.append(line)
    if("alternanciaCircular" in linhas[0]):
        linha1 =  (linhas[0].split("|"))
        linhaNovo =[]
        linhas.pop(0)
        for i in linhas:
            i =  i.split("|")
            copia = str(i[0])+"|"+str(i[1])+"|"+str(i[2])+"|"+str(i[3])+"|"+str(i[4])+"|"+str(i[5])+"|"+str(0) 
            linhaNovo.append(copia)
        alternanciaCircular(linhaNovo,linha1[1])
    elif ("loteria" in linhas[0]):
        loteria(linhas)
    elif ("prioridades" in linhas[0]):
        prioridades(linhas)

# no loteria é quantos bilheres o processo tem 
def loteria(linhas):
    print("no loterias")
    bilhetes = []
    linhas.pop(0)
    somabilhetes = 0
    for n in linhas:
        quebra = n.split('|')
        while int(quebra[3]) != 0:
            quebra.append()

        bilhetes.append(quebra[3])
        somabilhetes = somabilhetes + int(quebra[3])
    #print(bilhetes)
    print(somabilhetes)
def prioridades(linhas):
    print("no prioridades")

if __name__ == "__main__":
    main()
