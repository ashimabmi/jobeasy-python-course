# FOR LOOPS EXERCISES

# Ex. 1
# Enter your name, save it in name variable and save in result_1 variable your name repeated 3 times (use loops)

name_1 = input('enter your name:')
count = 0
while count < 3:
    result_1 = name_1
    count = count+1
    print(result_1)

# TODO: Here is your code

# Ex. 2
# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then save in result_2 variable your name repeated as many times as number_1 is
# (use loops)
name_2 = input('enter your name:')
number_1 = int(input('enter a number:'))
count = 0
while count < number_1:
    result_2 = name_2
    count = count+1
    print(result_2)

# TODO: Here is your code

# Ex. 3
# Enter a random string, which includes only digits. Write code which find a sum of digits in this string and save it
# into result_3 variable

string_number_1 = input('enter a string of digits:')
result_3 = 0
for digit in string_number_1:
    result_3 = result_3 + int(digit)
print(result_3)

# TODO: Here is your code

# Ex. 4
# Create code which sums up all even numbers between 2 and 100 (include 100) and save it in result_4 variable
number = range(2, 101)
result_4 = 0
index = 0
while index < len(number):
    if number[index] % 2 == 0:
        result_4 = result_4 + number[index]
    print('this is index', index)
    print('this is value', number[index])
    print('this is result', result_4)
    index = index + 1




#print(result_4)



#result_4 = None

# TODO: Here is your code