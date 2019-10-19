from time import time

def Primes_Gen(data, save):
    data = data.readlines()
    primes = []

    for i in data:
        primes.append(int(i))


    while True:

        t = time()
        L = len(primes)
        A = primes[-1]+2
        while len(primes) == L:
            if all([A%x != 0 for x in primes]):
                primes.append(A)

            else:
                A += 2
        print(L+1)
        print(str(int((time()-t)*1000)/1000) + "s")
        save.write(str(A)+"\n")

data = open("database.txt", "r")

save = open("database.txt", "a")

Primes_Gen(data, save)
