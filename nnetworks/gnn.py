import math
import random

# CONSTANTS
MAX_TRAINING_POINTS = 8
MAX_IN = 16
MAX_NUM_NEURONS = 32
MAX_NUM_LAYERS = 16

OFF = 0
ON = 1

TANH = 0
EXP = 1
ID = 2
POL1 = 3
POL2 = 4

LINEAR = 0
LEGENDRE = 1
LAGUERRE = 2
FOURIER = 3

L2 = 0
LINF = 1
COS = 2

PI = 3.131592654

neuron =[0,
         [0 for i in range(MAX_IN)],
         0,
         0,
         [0 for i in range(MAX_IN)],
         [0 for i in range(MAX_IN)],
         0]
NEURON = [neuron for i in range(MAX_NUM_NEURONS)]
NETWORK = [0,
           [0 for i in range(MAX_NUM_LAYERS)],
           [[0 for i in range(MAX_NUM_LAYERS)] for i in range(MAX_NUM_NEURONS)]]

NNUM = 0
NDATA = 0
ISEED = 0
WMIN = 0
WMAX = 0
X = []
Y = []

def rnd():
    ISEED = math.fmod(1027.,1048576.)
    return (ISEED/1048576)

def load():
    return

def save():
    return

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
        
def binom(n,k):
    return

def randomize():
    return

def activation(typ,x):
    return

def feedforward():
    return

def error(typ):
    return

def random_search(output, nmax, eps):
    return

def simulated_annealing(output,mmax,nmax,kbtmin,kbtmax,eps):
    return

def gradient_descent(output,nxw,maxiter,gamma,eps):
    return

def genetic_algorithm(output,nmap,npop,rate,eps):
    return

def main():
    ISEED = 38467.

    NDATA = 3

    X[0] = 0.15; 
    X[1]
