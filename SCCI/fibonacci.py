def fibo(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   return fibo(n-1) + fibo(n-2)




def fibo_iterative(n):
   a,b = 0,1
   for i in range(n):
       a,b = b,a+b
   return a



# recursive fibonacci with memory
memo = {0:0,1:1}
def fibo_memory(n):
    if not n in memo:
        memo[n] = fibo_memory(n-1) + fibo_memory(n-2)
    return memo[n]
