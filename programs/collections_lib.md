
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
     
     
 # collections.deque
 
 (like made of linked list)
 
 Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.


 Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

Deque objects support the following methods:

append(x) <br>
Add x to the right side of the deque.

appendleft(x) <br>
Add x to the left side of the deque.

clear() <br>
Remove all elements from the deque leaving it with length 0.

count(x) <br>
Count the number of deque elements equal to x.

New in version 2.7.

extend(iterable) <br>
Extend the right side of the deque by appending elements from the iterable argument.

extendleft(iterable) <br>
Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

pop() <br>
Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

popleft() <br>
Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

remove(value) <br>
Remove the first occurrence of value. If not found, raises a ValueError.

New in version 2.5.

reverse() <br>
Reverse the elements of the deque in-place and then return None.

New in version 2.7.

rotate(n=1) <br>
Rotate the deque n steps to the right. If n is negative, rotate to the left.

When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft()).

Deque objects also provide one read-only attribute:

maxlen <br>
Maximum size of a deque or None if unbounded.


In addition to the above, deques support iteration, pickling, len(d), reversed(d), copy.copy(d), copy.deepcopy(d), membership testing with the in operator, and subscript references such as d[-1]. Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.





---
