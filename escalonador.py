from alternancia import alternanciaCircular
from loteria import loteria
from prioridades import prioridades
import logging
import threading
import time

def thread_function(id):
    logging.info("Thread %s: starting", id)
    print("Digite o novo processo:")
    novo = input()    
    logging.info("Thread %s: finishing", id)

def main():
    threads = [] #armazena os descritores das threads

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    t = threading.Thread(target=thread_function, args=(1)) #inicializa a thread, informa o nome da função e os parâmetros
    logging.info("Main    : before running thread")
    t.start()
    threads.append(t)
    t = threading.Thread(target=escolheEscalonador, args=()) #inicializa a thread, informa o nome da função e os parâmetros
    t.start()
    threads.append(t)
    logging.info("Main    : wait for the thread to finish")

    for t in threads:
        t.join()

    logging.info("Main    : all done")

def escolheEscalonador():
    linhas =[] 

    while(True):
        print("Qual tipo de escalonador voce deseja usar? 0 - para alternancia 1 - para loteria 2 - para prioridades")
        escalonador =0
        if(escalonador==0):
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
        elif(escalonador==1):
            
                loteria(linhas)
        elif (escalonador == 2):
            linha1 =  (linhas[0].split("|"))
            linhaNovo =[]
            linhas.pop(0)
            for i in linhas:
                i =  i.split("|")
                copia = str(i[0])+"|"+str(i[1])+"|"+str(i[2])+"|"+str(i[3])+"|"+str(i[4])+"|"+str(i[5])+"|"+str(0) 
                linhaNovo.append(copia)
            prioridades(linhaNovo, linha1[1])
# no loteria é quantos bilheres o processo tem 


if __name__ == "__main__":
    main()
