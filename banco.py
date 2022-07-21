import logging
import threading
import time
lock = threading.Lock()
#for com n threads
#random da conta e da operação e do valor
#lista de mutexes e de semaforos para cada conta

def transacoes(id, conta, tipo,valor):

    while True:
        lock.acquire()
        logging.info("Thread %s pegou o lock e vai dormir %s %s %s ", id, conta,tipo, valor)
        if(tipo == "C"):
            conta=conta+valor
        if(tipo == "D"):
            conta= conta-valor
        time.sleep(1)
        logging.info("Thread %s acordou", id)
        lock.release()
        logging.info("Lock liberado")

def leitura():
    while True:
        logging.info("Na leitura")


if __name__ == "__main__":

    threads = [] #armazena os descritores das threads

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    contas={1:100, 2:50,3:500}
    print(contas[1])
    for id in range(1,3):
        tipo="C"
        valor=10
        t = threading.Thread(target=transacoes, args=(id,contas[1], tipo,valor)) 
        logging.info("Main    : before running thread")
        t.start()
        threads.append(t)
        tL = threading.Thread(target=leitura, args=()) 
        tL.start()
        threads.append(tL)
    for t in threads:
        t.join()

    logging.info("Main    : all done")