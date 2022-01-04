
from numpy import double


def fromFile(fileName = 'in.txt'):
    info = {}
    f = open(fileName,'r')
    info['no of Equations'] = int(f.readline())
    info['method'] = f.readline().replace('\n','')
    info['equations'] = []
    for k in range(info['no of Equations']):
        info['equations'].append(f.readline().replace('\n',''))

    if info['method'] == 'Gaussian-jordan':
        info['initial values'] = f.readline().split()
        for k in range(info['no of Equations']):
            info['initial values'][k] = double(info['initial values'][k])
    return info