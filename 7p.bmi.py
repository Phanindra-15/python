height = float(input('Enter your height in cms : '))
weight = float(input('Enter your weight in kgs : '))
height *= 0.01    
bmi = weight / (height * height)
print('Your Body Mass Index is - ', bmi)
