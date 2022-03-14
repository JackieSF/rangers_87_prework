# prework questions and solutions
#question 1: write a function that prints "hello_USERNAME"

def hello_name(user_name):
    print("hello_" + user_name.upper() + "!" )
    return user_name
hello_name('Terell')  

#question 2: Print first odd numbers between 1 and 100
def first_odds():
    """
        print all the odd numbers between 1 and 100
    """

    current_number = 0

    while current_number < 100:
        if current_number % 2 == 1:
            print(current_number)
            current_number += 1
    
first_odds()

#question 3: write a function that returns the max number in a given list
def max_num_in_list(a_list):
    """
    returns largest number in a list.
    """

    max_number = max(a_list)
    return max_number

number_list = [12,470,73,88,65,49]

def max_num_2(a_list):
    return max(a_list)

print(max_num_in_list(number_list))
print(max_num_2(number_list))


#Questions 4: write a function that returns true oif the given year is a leap year
def is_leap_yea(a_year):
    num = a_year
    if num % 400 == 0:
        print(True)
    elif num % 4 == 0 and num % 100 != 0:
        print(True)
    else:
        print(False)

def leap_year_2(a_year):
    """
        Return whether a given year is a leap year
    """
    return(a_year % 4 == 0 and a_year % 100 != 0)

    is_leap_year(2024)
    print(leap_year_2(2000))

#Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    if  len(a_list) > 1:
        for number in range(len(a_list)):
            if a_list[number] == a_list[number +1] -1:
                return True
            else:
                return False

print("is this consecutive:",is_consecutive([1,2,3,5,6,7]))