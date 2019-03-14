
print("\nWith list comprehension")

my_nums  = [ x*x for x in [1,2,3,4,5]]
print(my_nums)



print("\nWith GENERATORS  - replace square brackets with parentheses")



my_nums  = ( x*x for x in [1,2,3,4,5] )
print(my_nums)

# use generator only once , below 2nd print wont work after 1st runs

for num in my_nums:
    print(num)

print(list(my_nums))    # on converting generator into list, you lose the advantages you gained in terms of performance
                        # because generators are not holding all the values in memory



print("\n\nOther variants")
print("\nlist function")
my_nums  = list( x*x for x in [1,2,3,4,5] )
print(my_nums)

print("\nlist( () )")
my_nums  = list( (x*x for x in [1,2,3,4,5]) )
print(my_nums)