from ast import Delete
from random import sample
from alternancia import alternanciaCircular
from loteria import loteria
from prioridades import prioridades
import logging
import threading
import time
from loteria import loteria
def thread_function(id):
    logging.info("Thread %s: starting", id)
    time.sleep(2)
    logging.info("Thread %s: finishing", id)
def main():
    linhas =[] 
    with open("loteria.txt", "r") as tf:
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

        
        #copia = str(n[0])+"|"+str(n[1])+"|"+str(diminuiTempo)+"|"+str(n[3])+"|"+str(original[4])+"|"+str(original[5])+"|"+str(int(original[6])+1) 

def prioridades(linhas):
    print("no prioridades")

if __name__ == "__main__":
    main()
