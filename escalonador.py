import random
def main():
    linhas =[] 
    with open("loteria.txt", "r") as tf:
        lines = tf.read().split('\n')        
    for line in lines:
        linhas.append(line)
    if("alternanciaCircular" in linhas[0]):
        alternanciaCircular(linhas)
    elif ("loteria" in linhas[0]):
        loteria(linhas)
    elif ("prioridades" in linhas[0]):
        prioridades(linhas)

def alternanciaCircular(linhas):
    print("entrou")

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
