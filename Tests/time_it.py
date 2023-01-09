from Algorithm.christofides import *
from Algorithm.graph import *
import time
import random
def genereta_graph(n):
    supp=[[random.randint(1, 99),random.randint(1, 99)] for i in range(n)]
    return graph(supp,coordinates=1)

def time_it(n):
    gr=genereta_graph(n)
    start = time.time()
    christofides(gr)
    end = time.time()
    return end-start


for i in [25,50,100,150,200,300,500,1000]:
    print("dla danych wielkosci n="+str(i)+" czas na wykonianie alg wynosi "+str(round(time_it(i),4))+" sekund")


