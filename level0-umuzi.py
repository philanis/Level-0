##Task 0.1
print("Task0.1")
x = 0
y = 1
print(x)
print(y)
   
x = x + 3
y = y + x
print(x)
print(y)


##Task 0.2
print("Task0.2")
x = 1+1*2
y = (1+1)*2
z = 1 + (1*2)
a = 1+1*2/2
b = (1+1*2)/2
print(x)
print(y)
print(z)
print(a)
print(b)


##Task 0.3
print("Task 0.3")
def hello(name):
    print("Hello " +  name + "!")
hello("Nhlaka")

##Task 0.4
print("Task 0.4")
def even_or_odd(num):
    if (num%2 == 0):
        print("even")
    else:
        print("odd")    
even_or_odd(89)


##Task 0.5
print("Task 0.5")
def area_of_triangle(x,y,z):
    s = (x+y+z)/2
    area = (s*(s-x)*(s-y)*(s-z))**0.5
    print(area)
area_of_triangle(4,5,7)

##Task 0.6
print("Task 0.6")
def max_number(a,b,c):
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c
    print(largest)
max_number(12,10,7)

##Task 0.7
print("Task 0.7")
def celsius_to_fahrenheit(c):
    fahrenheit = (c*9/5)+32
    print(fahrenheit)
celsius_to_fahrenheit(60)

def fahrenheit_to_celsius(f):
    celsius = (f-32)*5/9
    print(celsius)
fahrenheit_to_celsius(140)

#Task 0.8
print("Task 0.8")
def convert_to_hours(num):
    print(str(num//60) +" hours")
    print(str(num%60) + " minutes")
convert_to_hours(133)



##Task 0.9
print("Task 0.9")
def vowels(word) :
    if 'a' in word:
        print('a')
    if 'e' in word:
        print('e')
    if 'i' in word:
        print('i')
    if 'o' in word:
        print('o')
    if 'u' in word:
        print('u')
    
vowels("monkey")

##Task 0.10
print("Task 0.10")
def common_letters(a,b):
    s1 = set(a)
    s2 = set(b)
    common = s1 & s2
    print(common)
common_letters("house", "computers")
