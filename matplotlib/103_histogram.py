import matplotlib.pyplot as plt


# histogram have quantitative variables(frequency distribution of data in bins)  while bar graph have categorical variables


population_ages = [22,66,88,4,5633,23,3,56,96,53,89,32,8,32,86,42,42,65,67,88,22,99,55,88,33,77,32,75,34,55,77,89,99,43,66,64,102,48,103]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins, histtype='bar', rwidth=0.8)


plt.xlabel("Age groups")
plt.ylabel("Ages")
plt.title("Histogram")
plt.legend()


plt.show()




