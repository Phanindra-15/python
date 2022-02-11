name = input('Enter name : ')
maths = int( input('Enter marks in maths : ')) 
physics = int( input('Enter marks in physics : ')) 
chemistry = int( input('Enter marks in chemistry : ')) 
total_marks =  maths + physics + chemistry
percentage = (total_marks / 300) * 100
print(name,  percentage)
