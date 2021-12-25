# Importing NumPy Library
import numpy as np
import sys


def gauss_elimination(number_of_equations,input_equations):
    solution = np.zeros(number_of_equations)

    # Applying Gauss Elimination
    for i in range(number_of_equations):
        if input_equations[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, number_of_equations):
            ratio = input_equations[j][i] / input_equations[i][i]

            for k in range(number_of_equations + 1):
                input_equations[j][k] = input_equations[j][k] - ratio * input_equations[i][k]

    # Back Substitution
    solution[number_of_equations - 1] = input_equations[number_of_equations - 1][number_of_equations] / input_equations[number_of_equations - 1][number_of_equations - 1]

    for i in range(number_of_equations - 2, -1, -1):
        solution[i] = input_equations[i][number_of_equations]

        for j in range(i + 1, number_of_equations):
            solution[i] = solution[i] - input_equations[i][j] * solution[j]

        solution[i] = solution[i] / input_equations[i][i]

    # Displaying solution
    return solution


def gauss_jordan(number_of_equations, input_equations):

    solution = np.zeros(number_of_equations)

    # Applying Gauss Jordan Elimination
    for i in range(number_of_equations):
        if input_equations[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(number_of_equations):
            if i != j:
                ratio = input_equations[j][i] / input_equations[i][i]

                for k in range(number_of_equations + 1):
                    input_equations[j][k] = input_equations[j][k] - ratio * input_equations[i][k]

    #  Obtaining Solution

    for i in range(number_of_equations):
        solution[i] = input_equations[i][number_of_equations] / input_equations[i][i]

    # Displaying solution
    return solution


def LU(number_of_equations, A):
    # n = len(A)  # Give us total of lines

    # (1) Extract the b vector
    b = [0 for i in range(number_of_equations)]
    for i in range(0, number_of_equations):
        b[i] = A[i][number_of_equations]

    # (2) Fill L matrix and its diagonal with 1
    L = [[0 for i in range(number_of_equations)] for i in range(number_of_equations)]
    for i in range(0, number_of_equations):
        L[i][i] = 1

    # (3) Fill U matrix
    U = [[0 for i in range(0, number_of_equations)] for i in range(number_of_equations)]
    for i in range(0, number_of_equations):
        for j in range(0, number_of_equations):
            U[i][j] = A[i][j]

    n = len(U)

    # (4) Find both U and L matrices
    for i in range(0, n):  # for i in [0,1,2,..,n]
        # (4.1) Find the maximum value in a column in order to change lines
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i + 1, n):  # Interacting over the next line
            if abs(U[k][i]) > maxElem:
                maxElem = abs(U[k][i])  # Next line on the diagonal
                maxRow = k

        # (4.2) Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, n):  # Interacting column by column
            tmp = U[maxRow][k]
            U[maxRow][k] = U[i][k]
            U[i][k] = tmp

        # (4.3) Subtract lines
        for k in range(i + 1, n):
            c = -U[k][i] / float(U[i][i])
            L[k][i] = c  # (4.4) Store the multiplier
            for j in range(i, n):
                U[k][j] += c * U[i][j]  # Multiply with the pivot line and subtract

        # (4.5) Make the rows bellow this one zero in the current column
        for k in range(i + 1, n):
            U[k][i] = 0

    n = len(L)

    # (5) Perform substitution Ly=b
    y = [0 for i in range(n)]
    for i in range(0, n, 1):
        y[i] = b[i] / float(L[i][i])
        for k in range(0, i, 1):
            y[i] -= y[k] * L[i][k]

    n = len(U)

    # (6) Perform substitution Ux=y
    x = [0 in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = y[i] / float(U[i][i])
        for k in range(i - 1, -1, -1):
            U[i] -= x[i] * U[i][k]

    return x


def gauss_seidel(A, b, tolerance=0.00001, max_iterations=50):
    x = np.zeros_like(b, dtype=np.double)

    # Iterate
    for k in range(max_iterations):

        x_old = x.copy()

        # Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1):], x_old[(i + 1):])) / A[i, i]

        # Stop condition
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break

    return x
