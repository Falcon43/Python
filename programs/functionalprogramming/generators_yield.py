print("Without generator")

def fibo_iterative_nogenerator(n):
    result = []
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        result.append(a)
    print(result)
    return

fibo_iterative_nogenerator(7)       # [1, 1, 2, 3, 5, 8, 13]


print("\nWith generators")

def fibo_iterative_generator(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        yield a      # for each number in range of numbers, yield the result


# print(next(fibo_iterative_generator(7)))

generator_object_notyetstartedcomputation = fibo_iterative_generator(7)

for after_next in generator_object_notyetstartedcomputation:
    print(after_next)




