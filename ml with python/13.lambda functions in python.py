Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def square(n):
    return n**2

x=square(7)
x
49
y=square(9)
y
81

l=[1,2,3,4,5]

x=list(map(square,l))

x
[1, 4, 9, 16, 25]

#lambda expression
--------------------------
SyntaxError: invalid syntax

# syntax:  lambda num(input) : num**2 (output)
lambda num:num**2
<function <lambda> at 0x0000020E3BA47910>

list(map(lambda num : num**2,l))
[1, 4, 9, 16, 25]
sq=lambda num:num**2
sq(2)
4
sq(5)
25

#we can have multiple inputs while declsring the inputs
asum = lambda x,y:x+y
asum(2,3)
5
asum(9,9)
18

#another way to define function with the help of this we should not  name of th finction and when we are needed we need to name of the functon

sub=lamda x,y:x-y
SyntaxError: invalid syntax. Perhaps you forgot a comma?
sub = lambda x,y :x-y
sub(4,2)
2
sub(2,4)
-2
sub(4,2)