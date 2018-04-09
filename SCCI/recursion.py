# recursion uses divide and conquer paradigm
# expensive(inefficient) - takes up lot of time and memory
# we must avoid infinite recursion

import time


print("\nFactorial  |  time efficiency  |  recursion  vs  list \n")

def fact(x):
    if x == 0 or x ==1:
        return 1
    return x * fact(x-1)



num = int(input("Enter a number: "))
if num < 0:
    raise Exception("Enter positive number!")
else:
    start = time.time()
    print("The factorial of ",num," is ",fact(num))

print("\nspeed of RECURSION during factorial: ")
print((time.time()-start)*1000)



start = time.time()

factorial = 1
for f in list(range(1,num+1)):
    factorial = factorial*f
print("The factorial of ",num," is ",factorial)

print("speed of LIST during factorial: ")
print((time.time()-start)*1000)





print("\n\n\nFibonacci  |  time efficiency  |  recursion  vs  list \n")

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)



start = time.time()
print("Fibonacci number using RECURSION at ",num," is ",fibo(num))
print((time.time()-start)*1000)



def fibo_iterative(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

start = time.time()
print("Fibonacci number using ITERATION at ",num," is ",fibo_iterative(num))
print((time.time()-start)*1000)





# recursive fibonacci with memory
memo = {0:0,1:1}
def fibo_memory(n):
    if not n in memo:
        memo[n] = fibo_memory(n-1) + fibo_memory(n-2)
    return memo[n]



start = time.time()
print("Fibonacci number using RECURSION  with MEMORY at ",num," is ",fibo_memory(num))
print((time.time()-start)*1000)
