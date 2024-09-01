import datetime
# # Calculate your age based on the current year and your birth year.
def age(bYear:int):
    currentYear:int=datetime.datetime.now().year
    a:int=currentYear-bYear
    return(a)
birthYear:int=int(input("Please enter your birth year : "))
age_cal:int=age(birthYear)
print(f"Your age is : {age_cal}")

#  #  - Write a program that calculates the area of a rectangle using length and width variables.
def area(l:int,w:int):
    return(l*w)
length:int=int(input("enter lenghth of rectangle : "))
width:int=int(input("enter width of the rectangle : "))
result:int=area(length,width)
print(f"the Area of rectangle is : {result}")

# #  - Write a program that calculates the area of a circle.
def circle_area(r:int):
    return(3.14*r)
radius:int= int(input("Enter the radius of the circle : "))
area:int= circle_area(radius)
print(f"The Radius of circle is : {area}")

# #  -Write a program that calculates the area of the cube.
def cube_area(a:int):
    return(6*a**2)
side:int = int(input("Enter the one side lenghth of cube : "))
area:int=cube_area(side)
print(f"Area of cube is : {area}")

# #  - Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
def temp_f(t:int):
    return((t-32)* (5/9))
def temp_c(t:int):
    return(((9/5)*t)+32)

temp:int= int(input ("Enter temperature in Farenheit : "))
temp1:int= temp_f(temp)
print(f"the temperature in Celsius is : {temp1}")

tp:int= int(input ("Enter temperature in Celsius : "))
temp1:int =temp_c(tp)
print(f"the temperature in Fahrenheit is : {temp1}")

# #  - Convert a given number of seconds into minutes and seconds using variables.
def min_sec(time:int):
    mins:int=time//60
    seconds:int=time%60
    print(f"the minutes are :{mins} and  the seconds are : {seconds}")

sec:int= int(input("Enter time in seconds : "))
min_sec(sec)

# #  - Write a program that calculates the percentage.
def get_percentage(v:int,p:int):
    return(v/100*p)
value:int= int(input("Enter the Value : "))
percentage:int= int(input("Enter the percentage value : "))
result:int=get_percentage(value,percentage)
print(f"the percentage is: {result}")

# #Write a program that calculates the BMI using height and weight variables
def get_BMI(h:int,w:int):
    return(w/h)
height:int= int(input("Enter the height of person in meters: "))
weight:int= int(input("Enter the weight of person in kgs: "))
result:int=get_BMI(height,weight)
print(f"the BMI of the person is : {result}")

# #write a program that calculates the volume of a cylinder using the formula
def area_cylinder(r:int,h:int):
    return(3.14*(r*r)*h)
radius:int= int(input("Enter the radius of the cylinder : "))
height:int=int(input("Enter the height of the cylinder : "))
area:int= area_cylinder(radius,height)
print(f"The Area of cylinder is : {area}")