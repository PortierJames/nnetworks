##
##   Python3 version of gneural_network. Please see below for the full details.
##
##   gneural_network is the GNU package which implements a programmable neural network.
##
##   Copyright (C) 2016 Jean Michel Sellier
##   <jeanmichel.sellier@gmail.com>
##
##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 3, or (at your option)
##   any later version.
##
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.
##
##   You should have received a copy of the GNU General Public License
##   along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
X = [0 for i in range(MAX_TRAINING_POINTS)]
Y = [0 for i in range(MAX_TRAINING_POINTS)]

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

    X[0] = 0.15 
    X[1] = 0.60
    X[2] = 0.80
    Y[0] = math.sqrt(X[0])
    Y[1] = math.sqrt(X[1])
    Y[2] = math.sqrt(X[2])

    WMIN = -1.
    WMAX = +1.

    NNUM = 6

    NEURON[0][0] = 1
    NEURON[1][0] = 1
    NEURON[2][0] = 1
    NEURON[3][0] = 1
    NEURON[4][0] = 1
    NEURON[5][0] = 4

    NEURON[0][2] = ID
    NEURON[1][2] = TANH
    NEURON[2][2] = TANH
    NEURON[3][2] = TANH
    NEURON[4][2] = TANH
    NEURON[5][2] = TANH

    NEURON[0][3] = LINEAR
    NEURON[1][3] = LINEAR
    NEURON[2][3] = LINEAR
    NEURON[3][3] = LINEAR
    NEURON[4][3] = LINEAR
    NEURON[5][3] = LINEAR

# defines the topology of the network
    NETWORK[0] = 3
    
    NETWORK[1][0] = 1
    NETWORK[1][1] = 4
    NETWORK[1][2] = 1
    
    NETWORK[2][0][0] = 0
    
    NETWORK[2][1][0] = 1
    NETWORK[2][1][1] = 2
    NETWORK[2][1][2] = 3
    NETWORK[2][1][3] = 4
    
    NETWORK[2][2][0] = 5

# defines the connections between the neurons
    NEURON[1][1][0] = 0
    NEURON[2][1][0] = 0
    NEURON[3][1][0] = 0
    NEURON[4][1][0] = 0
    NEURON[5][1][0] = 1
    NEURON[5][1][1] = 2
    NEURON[5][1][2] = 3
    NEURON[5][1][3] = 4

    randomize()

    simulated_annealing(ON,25,25000,1.e-4,8.,1.e-2)

    nx = 32
    MIN = 0.
    MAX = 1.

    for n in range(nx):
        x = MIN+(n+0.5)*(MAX-MIN)/nx
        y = math.sqrt(x)
        NEURON[0][5][0] = x
        NEURON[0][6] = x
        feedforward()
        r = NEURON[5][6]
        print(x,y,r)

    return 0

if __name__ == "__main__":
    main()
