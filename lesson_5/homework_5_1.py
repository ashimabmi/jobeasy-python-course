# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1, num_2):
    diff = num_1 - num_2
    return diff
d1 = difference(6, 3)
print(d1)


# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    div = num_1/num_2
    return div
div_1 = division(4,2)
print(div_1)


# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

def function_1(number):
    if number > 10:
        d1 = 100 - number
        return d1
    else:
        d1 = number * 10
        return d1
num = function_1(10)
print(num)




# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temperature_convertor(fahrenheit_degree):
    temp_celsius = (fahrenheit_degree - 32) * 5/9
    return temp_celsius
tem_c = temperature_convertor(98)
print(round(tem_c))

# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
    t_1 = 4 + (25/14) * distance
    t_2 = round(t_1, 2)
    return t_2
t_3 = taxi_fare(10)
print(t_3)

# examples of usage:
# taxi_fare(10) #21.86