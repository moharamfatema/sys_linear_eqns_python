import sympy as sp
import numpy as np
NO_EQNS = 'no of Equations'
INIT = 'initial values'


def from_file(file_name = 'in.txt'):
    info = {}
    f = open(file_name,'r')
    info[NO_EQNS] = int(f.readline())
    info['method'] = f.readline().replace('\n','')
    info['equations'] = []
    for k in range(info[NO_EQNS]):
        info['equations'].append(f.readline().replace('\n',''))

    if info['method'] == 'Gaussian-siedel' or info['method'] == 'All':
        info[INIT] = f.readline().split()
        for k in range(info[NO_EQNS]):
            info[INIT][k] = np.double(info[INIT][k])
    
    info['max iterations'] = 50
    info['epsilon'] = 1e-5
    return info

def get_coeff(info):
    syms = sp.symbols('a:z')
    syms = syms[0:info[NO_EQNS]]
    eqns = sp.sympify(info['equations'])
    a = []
    for i in range(info[NO_EQNS]):
        a.append([])
        for k in  range(info[NO_EQNS]):
            a[i].append(eqns[i].coeff(syms[k]))
            eqns[i] = eqns[i] - eqns[i].coeff(syms[k])*syms[k]
    
    a = np.asarray(a)
    b = -1 * np.double(eqns)

    aug = np.concatenate((a ,np.array([b]).T),axis=1)

    return a,b,aug