from random import randrange
import time

def processo_1( index : int, tempo : int, num : int = 100):
    start = tempo
    sort = 0
    for i in range(index):
        sort = randrange(0, 10)
    for i in range(index, num):
        sort = randrange(0, 10)
        print(f"Sorteador doido (i={i}): {sort}")
        yield i+1
    end = time.perf_counter()
    print(f"tempo de execução do processo: {end - start:.6f} segundos")
    return True

#
def processo_2( index : int, tempo : int, num : int = 100):
    start = tempo
    array = [i for i in range(num)]
    for i in range(1, index):
        array[i - 1] = array[i]
    for i in range(index+1, num):
        print(f"Movedor insano (i={i-1}): {array[i - 1]} = {array[i]}")
        array[i - 1] = array[i]
        yield i
    array[-1] += 1
    end = time.perf_counter()
    print(f"tempo de execução do processo: {end - start:.6f} segundos")
    return True

def processo_3(index : int, tempo : int, num: int = 100):
    start = tempo
    cont = 0
    for i in range(index):
        if i % 2 == 0:
            cont += 2
        else:
            cont -= 1
    for i in range(index, num):
        if i % 2 == 0:
            cont += 2
        else:
            cont -= 1
        print(f"Contador maluco (i={i}): {cont}")
        yield i+1
    end = time.perf_counter()
    print(f"tempo de execução do processo: {end - start:.6f} segundos")
    return True