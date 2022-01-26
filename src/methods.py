# Importing NumPy Library
import numpy as np
import time


def gauss_elimination(number_of_equations,input_equations):
    solution = np.zeros(number_of_equations)
    data = {}
    data['Forward Elimination'] = []
    start = time.perf_counter() * 1000
    # Applying Gauss Elimination
    for i in range(number_of_equations):
        if input_equations[i][i] == 0.0:
            data['status'] = 'Error'
            data['exception'] = ZeroDivisionError
            raise ZeroDivisionError('Divide by zero detected!')

        for j in range(i + 1, number_of_equations):
            ratio = input_equations[j][i] / input_equations[i][i]  

            for k in range(number_of_equations + 1):
                input_equations[j][k] = input_equations[j][k] - ratio * input_equations[i][k]
            
            data['Forward Elimination'].append(np.copy( input_equations))



    # Back Substitution
    solution[number_of_equations - 1] = input_equations[number_of_equations - 1][number_of_equations] / input_equations[number_of_equations - 1][number_of_equations - 1]

    for i in range(number_of_equations - 2, -1, -1):
        solution[i] = input_equations[i][number_of_equations]

        for j in range(i + 1, number_of_equations):
            solution[i] = solution[i] - input_equations[i][j] * solution[j]

        solution[i] = solution[i] / input_equations[i][i]
    data['time'] = time.perf_counter() * 1000 - start 
    # Displaying solution
    data['solution'] = solution
    data['status'] = 'Good'
    return data


def gauss_jordan(number_of_equations, input_equations):


    data = {}
    data['Gaussian Jordan'] = []
    start = time.perf_counter() * 1000
    solution = np.zeros(number_of_equations)

    # Applying Gauss Jordan Elimination
    for i in range(number_of_equations):
        if input_equations[i][i] == 0.0:
            data['status'] = 'Error'
            data['exception'] = ZeroDivisionError
            raise ZeroDivisionError('Divide by zero detected!')

        for j in range(number_of_equations):
            if i != j:
                ratio = input_equations[j][i] / input_equations[i][i]

                for k in range(number_of_equations + 1):
                    input_equations[j][k] = input_equations[j][k] - ratio * input_equations[i][k]
                    data['Gaussian Jordan'].append(np.copy(input_equations))

    #  Obtaining Solution

    for i in range(number_of_equations):
        solution[i] = input_equations[i][number_of_equations] / input_equations[i][i]
    data['time'] = time.perf_counter() * 1000 - start
    data['solution'] = solution
    data['status'] = 'Good'
    # Displaying solution
    return data


def lu_decomposition(number_of_equations, input_equations):

    data = {}
    data['L'] = []
    data['U'] = []
    start = time.perf_counter() * 1000

    b = [0 for _ in range(number_of_equations)]
    L = [[0 for _ in range(number_of_equations)] for _ in range(number_of_equations)]
    U = [[0 for _ in range(0, number_of_equations)] for _ in range(number_of_equations)]
    
    L = np.array(L)
    U = np.array(U)

    for i in range(0, number_of_equations):
        # (1) Extract the b vector
        b[i] = input_equations[i][number_of_equations]

        # (2) Fill L matrix and its diagonal with 1
        L[i][i] = 1

        # (3) Fill U matrix
        for j in range(0, number_of_equations):
            U[i][j] = input_equations[i][j]


    n = len(U)

    # (4) Find both U and L matrices
    for i in range(0, n):  # for i in [0,1,2,..,n]
        # (4.1) Find the maximum value in a column in order to change lines
        max_elem = abs(U[i][i])
        max_row = i
        for k in range(i + 1, n):  # Interacting over the next line
            if abs(U[k][i]) > max_elem:
                max_elem = abs(U[k][i])  # Next line on the diagonal
                max_row = k

        # (4.2) Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, n):  # Interacting column by column
            tmp = U[max_row][k]
            U[max_row][k] = U[i][k]
            U[i][k] = tmp

        # (4.3) Subtract lines
        for k in range(i + 1, n):
            c = -U[k][i] / float(U[i][i])
            L[k][i] = c  # (4.4) Store the multiplier
            for j in range(i, n):
                U[k][j] += c * U[i][j]  # Multiply with the pivot line and subtract
            data['L'].append(np.copy(L))
            data['U'].append(np.copy(U))
            
        # (4.5) Make the rows bellow this one zero in the current column
        for k in range(i + 1, n):
            U[k][i] = 0
        
        data['U'].append(np.copy(U))

    n = len(L)

    # (5) Perform substitution Ly=b
    y = [0 for _ in range(n)]
    for i in range(0, n, 1):
        y[i] = b[i] / float(L[i][i])
        for k in range(0, i, 1):
            y[i] -= y[k] * L[i][k]

    n = len(U)

    # (6) Perform substitution Ux=y
    x = [0 for _ in range(n)]
    x = np.array(x)
    for i in range(n - 1, -1, -1):
        x[i] = y[i] / float(U[i][i])
        for k in range(i - 1, -1, -1):
            U[i] -= x[i] * U[i][k]

    data['time'] = time.perf_counter() * 1000 - start
    data['solution'] = np.asarray(x)
    return data


def gauss_seidel(a, b,initial_guesses, tolerance=0.00001, max_iterations=50):
    data = {}
    data['epsilon'] = []
    start = time.perf_counter() * 1000
    x =  initial_guesses.copy()
    data['x'] = [x.copy()]
    x = np.array(x)
    # Iterate
    data['iterations'] = 0
    for _ in range(max_iterations):
        data['iterations'] += 1
       #should the initial guesses be here?
        x_old = x.copy()

        # Loop over rows
        for i in range(a.shape[0]):
            first = b[i] or 0
            second = np.dot(a[i, :i], x[:i]) or 0
            third = np.dot(a[i, (i + 1):], x_old[(i + 1):]) or 0
            # print("b[i]= " + str(b[i]))
            # print("\nnp.dot(a[i, :i], x[:i])= " + str(np.dot(a[i, :i], x[:i])))
            # print("np.dot(a[i, (i + 1):], x_old[(i + 1):])= " + str(np.dot(a[i, (i + 1):], x_old[(i + 1):])))
            x[i] = (first - second - third) / a[i, i]
        data['x'].append(x.copy())

        # Stop condition
        #epsilon = np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
        epsilon = (x - x_old) / x 
        data['epsilon'] = epsilon
        flag = 0
        for value in epsilon:
            if value > tolerance:
                flag = 1
        if not flag:
            break
    data['solution'] = x
    data['time'] = time.perf_counter() * 1000 - start
    return data
