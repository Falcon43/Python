# timeit measures the amount of time it takes for a certain snippet of code to run
# does not get affected by any background (unrelated) process's time that time.time() may get affected by
# put all code of timeit inside  triple quotes , because it runs a process of it's own
import timeit

#print(timeit.timeit('1+3',number=50000000))



#input_list = range(1000)
#
#def div_by_five(num):
#    if num % 5 == 0:
#        return True
#    else:
#        return False
#
#
## Generator
#xyz = (i for i in input_list if div_by_five(i))
#
#for i in xyz:
#    abc = xyz
#
#
#
## List Comprehension
#xyz = [i for i in input_list if div_by_five(i)]
#abc = xyz




print('\n---------- Time efficiency  -  timeit ----------')
print("\nGenerator")
print(timeit.timeit('''input_list = range(1000)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


# Generator
xyz = (i for i in input_list if div_by_five(i))

for i in xyz:
    abc = xyz''', number=50000))





print("\nList Comprehension")
print(timeit.timeit('''input_list = range(1000)
                                                                         
def div_by_five(num):                                                    
    if num % 5 == 0:                                                     
        return True                                                      
    else:                                                                
        return False                                                     
                                                                         
                                                                         
# List comprehension                                                            
xyz = [i for i in input_list if div_by_five(i)]
abc = xyz''', number=50000))



