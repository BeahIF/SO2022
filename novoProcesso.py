import logging
import time
import threading
def thread_function(id):
    logging.info("Thread %s: starting", id)
    time.sleep(2)
    print("Digite o novo processo:")
    novo = input()
    
    
    logging.info("Thread %s: finishing", id)
