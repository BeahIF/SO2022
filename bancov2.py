import logging
import threading
import time
import random
contas={1:100, 2:50,3:500}

lock = threading.Lock()

def transacoes(id, saldo, tipo,valor, idConta):
    global contas
    print(saldo)
    print(tipo)
    print(valor)
    # while True:
    lock.acquire()
    logging.info("Thread %s pegou o lock e vai dormir %s %s %s ", id, saldo,tipo, valor)
    if(tipo == "C"):
        contas[idConta]=contas[idConta]+valor
    if(tipo == "D"):
        contas[idConta]= contas[idConta]-valor
    print("contas")
    print(contas)
    time.sleep(1)
    logging.info("Thread %s acordou", id)
    lock.release()
    logging.info("Lock liberado")
if __name__ == "__main__":
    threads = [] #armazena os descritores das threads

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    tipo=["D","C"]

    for id in range(1,3):
        tipoS = random.randint(0,1)
        valor=random.randint(0, 100)
        contaSorteada=[1,2,3]
        random.shuffle(contaSorteada)
        t = threading.Thread(target=transacoes, args=(id,contas[contaSorteada[0]], tipo[tipoS],valor, contaSorteada[0])) 
        logging.info("Main    : before running thread")
        t.start()
        threads.append(t)
        # tL = threading.Thread(target=leitura, args=()) 
        # tL.start()
        # threads.append(tL)
    for t in threads:
        t.join()

    logging.info("Main    : all done")