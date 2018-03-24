#  Given a string of brackets, determine if the string is balanced

from stack import Stack

def is_balanced(code_string):
    opening_brackets = ["{","[","(","<"]
    closing_brackets = ["}","]",")",">"]
    bracket_matches ={"}":"{","]":"[",")":"(",">":"<"}
    s = Stack()

    brackets_extracted = []
    for letter in code_string:
        if letter in opening_brackets or letter in closing_brackets:
            brackets_extracted.append(letter)

    for bracket in brackets_extracted:
        if bracket in opening_brackets:
            s.push(bracket)
        else:
            if bracket_matches[bracket] == s.peak():
                s.pop()
            else:
                return False

    return not s.size()





print(is_balanced("}{"))
print(is_balanced("{[<>]}"))
print(is_balanced("int numbers[ 100 ] = { 1, 2, 3, [10] = 10, 11, 12, [60] = 50, [42] = 420 };"))
print(is_balanced("for( i = 0; i < 20; i++ ) printf( \"Fibonacci[ %d ] = %f\n\", i, fibonacci[ i > );"))
print(is_balanced("int a[ 2 ][ 3 ] = { { 5, 6, 7 }, { 10, 20, 30 } }; int b[ 2 ][ 3 ] = { <{ 1, 2, 3 }, {  3,  2,  1 } };>  int sum[ 2 ][ 3 ], row, column;"))
print(is_balanced("cout << \"( Error codes are \" <<  err1 << \", \" << err2 << \", \" << err3   << \", \" << err4 << \", \" << err5 << \" )\n\" ;"))
print(is_balanced("#include <<stdlib.h>"))



"""
Output:

False
True
True
False
False
False
False


"""