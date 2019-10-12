file_name = "patanja.csv"
import random as rand

f = open(file_name, "r")

def make_sutra(file):
    f = file
    sutras = {}
    n = 0
    for i in f:
        n = n + 1
        spl = i.split(":")
        line = spl[1].strip('\n')
        sutras[n]=line
    f.close()
    return sutras

def surta_today(sutras):
    ran_key = rand.randint(1, len(sutras))
    sutra_today = sutras[ran_key]
    return sutra_today

sutras = make_sutra(f)
s=surta_today(sutras)