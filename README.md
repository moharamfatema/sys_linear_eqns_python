# Numerical Analysis Project 2: Systems of Linear Equations

# Contributors

- Fatema Moharam ID.6655
- Nourhan Waleed ID.6609
- Heba Elwazzan ID.6521

In this project, we are required to implement 4 numerical methods used to find the roots of a system of linear equations:

- Gaussian-elimination
- LU decomposition
- Gaussian-Jordan
- Gauss-Seidel

# Pseudocodes

## Gaussian-Elimination

```c
1. Start

2. Input the Augmented Coefficients Matrix (A):
	
	For i = 1 to n
		
		For j = 1 to n+1
			
			Read Ai,j
		
		Next j
	
	Next i

3. Apply Gauss Elimination on Matrix A:
	
	For i = 1 to n-1
		
		If Ai,i = 0
			
			Print "Mathematical Error!"
			Stop
		
		End If
		
		For j = i+1 to n
			
			Ratio = Aj,i/Ai,i
			
			For k = 1 to n+1
				
				Aj,k = Aj,k - Ratio * Ai,k
			
			Next k
		Next j
	Next i

4. Obtaining Solution by Back Substitution:
	
	Xn = An,n+1/An,n
	
	For i = n-1 to 1 (Step: -1)
		
		Xi = Ai,n+1
		
		For j = i+1 to n
			
			Xi = Xi - Ai,j * Xj
		
		Next j
		
		Xi = Xi/Ai,i
	Next i

5. Display Solution:
	
	For i = 1 to n
		
		Print Xi
	
	Next i

6. Stop
```

## LU Decomposition

![Untitled](Numerical%20Analysis%20Project%202%20Systems%20of%20Linear%20Equ%20a2ae68c3fc4f428faf39185e8f55623a/Untitled.png)

## Gaussian-Jordan

```c
1. Start

2. Input the Augmented Coefficients Matrix (A):
	
	For i = 1 to n
		
		For j = 1 to n+1
			
			Read Ai,j
		
		Next j
	
	Next i

3. Apply Gauss Jordan Elimination on Matrix A:
	
	For i = 1 to n
		
		If Ai,i = 0
			
			Print "Mathematical Error!"
			Stop
		
		End If
		
		For j = 1 to n
			
			If i ≠ j 
				
				Ratio = Aj,i/Ai,i
				
				For k = 1 to n+1
				
					Aj,k = Aj,k - Ratio * Ai,k
			
				Next k
				
			End If
			
		Next j
	Next i

4. Obtaining Solution:
	
	For i = 1 to n 
		Xi = Ai,n+1/Ai,i
	Next i

5. Display Solution:
	
	For i = 1 to n
		
		Print Xi
	
	Next i

6. Stop
```

## Gauss-Seidel

```c
1. Start

2. Arrange given system of linear equations in 
   diagonally dominant form

3. Read tolerable error (e)

4. Convert the first equation in terms of first variable, 
second equation in terms of second variable and so on. 

5. Set initial guesses for x0,  y0, z0 and so on

6. Substitute value of y0, z0 ... from step 5 in 
   first equation obtained from step 4 to calculate 
   new value of x1. Use x1, z0, u0 .... in second equation 
   obtained from step 4 to caluclate new value of y1. 
   Similarly, use x1, y1, u0... to find new z1 and so on.  

7. If| x0 - x1| > e and | y0 - y1| > e and | z0 - z1|  > e 
   and so on then goto step 9

8. Set x0=x1, y0=y1, z0=z1 and so on and goto step 6

9. Print value of x1, y1, z1 and so on

10. Stop
```

# Analysis of Performance

![Untitled](Numerical%20Analysis%20Project%202%20Systems%20of%20Linear%20Equ%20a2ae68c3fc4f428faf39185e8f55623a/Untitled%201.png)

LU decomposition seems to be the fastest method, but shows more error. Gauss-Seidel is the slowest, as it takes 17 iterations to reach desired accuracy. Gaussian-elimination and Gaussian-Jordan are comparable, with Gaussian-Jordan being the faster of the two.

# Sample Runs

## Gaussian-elimination

```c
2*a - 6*b - c + 38
-3*a - b + 7*c + 34 
-8*a + b - 2*c + 20
```

![Untitled](Numerical%20Analysis%20Project%202%20Systems%20of%20Linear%20Equ%20a2ae68c3fc4f428faf39185e8f55623a/Untitled%202.png)

## LU decomposition

```c
8*a + 4*b - c - 11
-2*a + 3*b + c - 4 
2*a - b + 6*c - 7
```

![Untitled](Numerical%20Analysis%20Project%202%20Systems%20of%20Linear%20Equ%20a2ae68c3fc4f428faf39185e8f55623a/Untitled%203.png)

## Gaussian-Jordan

```c
2*a + 3*b + c + 4
4*a + b + 4*c - 9 
3*a + 4*b + 6*c
```

![Untitled](Numerical%20Analysis%20Project%202%20Systems%20of%20Linear%20Equ%20a2ae68c3fc4f428faf39185e8f55623a/Untitled%204.png)

## Gauss-Seidel

```c
12*a + 23*b + 5*c - 1
a + 5*b + 3*c - 28
3*a + 7*b + 13*c - 76
1 0 1
```

![Untitled](Numerical%20Analysis%20Project%202%20Systems%20of%20Linear%20Equ%20a2ae68c3fc4f428faf39185e8f55623a/Untitled%205.png)