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

def prioridades(linhas):
    print("no prioridades")

if __name__ == "__main__":
    main()
