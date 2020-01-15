import math

# Problem 1
print("Problem 1 solution follows:")
a = 3
b = -5.86
c = 2.5408
R1 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
R2 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
print("Root 1:", R1)
print("Root 2:", R2)
print()

# Problem 2
print("Problem 2 solution follows:")
for i in range(2, 11):
    reciprocal = 1/i
    print("1/" + str(i) + ":", reciprocal)
print()

# Problem 3
print("Problem 3 solution follows:")
n = 10
triangular = 0
for i in range(1, n+1):
    triangular = triangular + i
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n*(n+1)/2)
print()

# Problem 4
print("Problem 4 solution follows:")
m = 10
factorial = 1
for j in range(1, m+1):
    factorial = factorial * j
print(str(m) + "!:", factorial)
print()

# Method 2 with recursion
# def factorial_recursive(m):
#     if m == 1:
#         return 1
#     else:
#         return m * factorial_recursive(m-1)
# factorial_recursive(10)
# print(str(m) + "!:", factorial)

# Method 3 with factorial function
# print(str(m) + "!:", math.factorial(m))

# Problem 5
print("Problem 5 solution follows:")
numlines = 10
for p in range(numlines, 0, -1):
    factorials = 1
    for q in range(1, numlines+1):
        factorials = factorials * q
    print(str(numlines) + "!:", factorials)
    numlines -= 1
print()

# Problem 6
print("Problem 6 solution follows:")
num = 10
summation = 1
for x in range(1, num+1):
    factor = 1
    for y in range(1, x+1):
        factor = factor * y
    summation = summation + 1/factor
print("e:", summation)
print()

# Collaboration
# None
