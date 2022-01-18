import sympy as sp
import numpy as np

from src.methods import gauss_elimination, gauss_jordan, gauss_seidel, lu_decomposition
NO_EQNS = 'no of Equations'
INIT = 'initial values'
AUG = 'Augmented matrix'


def dict_from_file(file_name = 'in.txt'):
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
    info['Coeff matrix'],info['B matrix'],info[AUG] = get_coeff(info)
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

def call_from_dict(info):
    method = info.get('mathod')
    if (method == 'Gaussian elimination'):
        return gauss_elimination(
            number_of_equations=info.get(NO_EQNS),
            input_equations=info.get(AUG)
        )
    elif (method == 'Gaussian Jordan'):
        return gauss_jordan(
            number_of_equations=info.get(NO_EQNS),
            input_equations=info.get(AUG)
        )
    elif (method == 'LU decomposition'):
        return lu_decomposition(
            number_of_equations=info.get(NO_EQNS),
            input_equations=info.get(AUG)
        )
    elif (method == 'Gaussian siedel'):
        return  gauss_seidel(
            a = info.get('Coeff matrix'),
            b = info.get('B matrix'),
            initial_guesses = info.get(INIT),
            max_iterations = info.get('max iterations'),
            tolerance = info.get('epsilon')
        )
    else:
        raise NotImplementedError

def call_from_file(file_name = 'in.txt'):
    info = dict_from_file(file_name)
    return call_from_dict(info)