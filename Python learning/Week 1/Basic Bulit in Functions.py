# We have alot of built-in functions . Bulit-in functins are available in python without importing anything

# Variables > store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated 

# Variables must include > 
# must start with a letter or underscore_
# Cannot start with a number 
# can only contain ( A - z, 0-9, and _ )
# Variables are case sensitive > age, Age, AGE are different variables

# Here is some examples of valid Variables
# > firstname lastname age country city first_name capital_city year_2021 birth_year num1 num2

#Here are INVALID variable names > first-name first@name first$name num-1 1num




# Assigning/Storing variables
firstname = 'Jason' 
last_name = 'fredo'
city = 'California'
age = 300 
is_married = False #give me 4 years
skills = ['Chicken', 'Beef', 'Pork']
Person_Info = {'firstname' : 'Chief', 'lastname' : 'Keef', 'age' : 300, 'Place of birth' : '79th and maryland'}

print('Bloodborne, game!')
print ('Hello',',',',',', World!')   #using comma will add space between the words
print(len(skills))

# Printing values stored in Variables 
print('firstname :', firstname)
print ( 'skills :', skills)
print ( 'Age > ', age)
print (firstname, last_name, city, age, Person_Info)

#                Declaring multiple  Variables in one line
firstname, last_name, city, age = 'Leonidas', 'Fredo', 'Miami', 300

print(firstname, last_name, city, age)

# Getting user input() bulit-in function

'''first_name = input ( 'What is your first name? ')
age = input ( 'How Young are you? ')

print (first_name)
print (age)'''


# Casting is > Converting 1 type of data type to another data

#float to int
gravity = -9.81
print (int(gravity))

# int to float
num6= 500
print (float(num6))

# str to int or float
num_days = '300'
print (int(num_days))
print (float (num_days))

# str to list 
first_name = 'diddy'
print(first_name)
first_name_list = list(first_name)
print(first_name_list)


First_name = 'burrrrrrerger'


height,weight,married = 5.10, 160, False
print((tuple),height, weight, married)

First_name = 'Bob'
Last_Name = 'Kat'

print(len(First_name))
print(len(Last_Name))

Nub_1 =5     
Nub_2 =4

print( Nub_1 + Nub_2)
total = Nub_1 + Nub_2
print(total)
print ( Nub_2 - Nub_1)
difference = Nub_2 - Nub_1
print(difference) 


# Caculate area of a circle using pi*r^2
PI = 3.14
Radius = 9.6

Area_of_Circle = PI * Radius ** 2
print(Area_of_Circle)

# Caculate the circumference of the circle

Circumference = 2 * PI * Radius
print(Circumference)

# Take radius as user input and calculate the area
Radius = float(input('Enter The Radius of the circle: '))
Area_of_Circle = input ('what is the area of the circle? : ')

