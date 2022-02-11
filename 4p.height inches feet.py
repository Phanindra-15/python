# WAP to enter height in inches and display them in feet and inches


height=int(input("enter the height in inches:"))
feet=height//12
inches=height%12
print(feet,"feet",inches,"inches")
