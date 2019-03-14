import random
import time

names = ['Joey','Rachel','Monica','Chandler','Pheobe','Ross']
majors = ['engineering','arts','computerscience','economics','humanities','dinosaur']

# print('Memory Before:  {}mb'.format(mem_profile.memory_usage_resource()))

print("\n\n---------Generators Time Efficiency -------\n")

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id' : i,
                    'name' : random.choice(names),
                    'major' : random.choice(majors)
        }
        result.append(person)
    return result



def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id' : i,
                    'name' : random.choice(names),
                    'major' : random.choice(majors)
        }
        yield person


num_peeps = 1000
start = time.time()
print(people_list(num_peeps))
print("Time taken by List : ", (time.time() -start)*1000)


start = time.time()
gen_op = people_generator(num_peeps)
for op in gen_op:
    print(op)
print("Time taken by Generators : ", (time.time() -start)*1000)
