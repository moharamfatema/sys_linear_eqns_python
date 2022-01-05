from sympy import *
import numpy as np


def fromFile(fileName = 'in.txt'):
    info = {}
    f = open(fileName,'r')
    info['no of Equations'] = int(f.readline())
    info['method'] = f.readline().replace('\n','')
    info['equations'] = []
    for k in range(info['no of Equations']):
        info['equations'].append(f.readline().replace('\n',''))

    if info['method'] == 'Gaussian-siedel' or info['method'] == 'All':
        info['initial values'] = f.readline().split()
        for k in range(info['no of Equations']):
            info['initial values'][k] = np.double(info['initial values'][k])
    
    info['max iterations'] = 50
    info['epsilon'] = 1e-5
    return info

def getCoeff(info):
    syms = symbols('a:z')
    syms = syms[0:info['no of Equations']]
    eqns = sympify(info['equations'])
    a = []
    for i in range(info['no of Equations']):
        a.append([])
        for k in  range(info['no of Equations']):
            a[i].append(eqns[i].coeff(syms[k]))
            eqns[i] = eqns[i] - eqns[i].coeff(syms[k])*syms[k]
    
    a = np.asarray(a)
    b = -1 * np.double(eqns)

    aug = np.concatenate((a ,np.array([b]).T),axis=1)

    return a,b,aug