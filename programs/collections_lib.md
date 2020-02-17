
# collections.Counter

"18077"
"78105"

s, g = collections.Counter(secret), collections.Counter(guess)<br>

Counter({'7': 2, '1': 1, '8': 1, '0': 1}) Counter({'7': 1, '8': 1, '1': 1, '0': 1, '5': 1})

b =  s & g <br>
print(b)

Counter({'1': 1, '8': 1, '0': 1, '7': 1})  # totally intersection of counts


b =  (s & g).values() <br>
        print(b)
        
dict_values([1, 1, 1, 1])

b =  sum((s & g).values()) <br>
        print(b)

4
        
   ---
        
