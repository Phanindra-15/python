Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=80
y=90

print('the value of x is',x)
the value of x is 80

print('the value of y is ',y)
the value of y is  90

print('the value of x and y is ',(x,y))
the value of x and y is  (80, 90)
print('the value of x is'+str(x)+'the value of y is'+str(y))


the value of x is80the value of y is90


print('i am going to inject %s here ' %'something')
i am going to inject something here 
print('i want to tell you %s that i hide ' %'one thing')
i want to tell you one thing that i hide 
print('the value of x is %s and value of y is %s,%(x,y)
      
SyntaxError: unterminated string literal (detected at line 1)
print('the value of x = %s and value of y = %s' %(x,y))
      
the value of x = 80 and value of y = 90
print("the value of x  is {},value of y is {}'.format(x,y))
      
SyntaxError: unterminated string literal (detected at line 1)
print("the value of x  is {},value of y is {}".format(x,y))
      
the value of x  is 80,value of y is 90
print("the value of x  is {1},value of y is {0}'.format(x,y))
      
SyntaxError: unterminated string literal (detected at line 1)
print("the value of x  is {1},value of y is {0}".format(x,y))
      
the value of x  is 90,value of y is 80
