
"""
Artificial Intelligence and Data Science
Assignment 01
"""




#Problem 01: Palindrome Checker
def is_palindrome(str):
    """
    Check if a string is palindrome or not
    A palindrome is a string/number that reads the same forward and backward (e.g 121, radar)

    Args:
    str: string to check
    
    Returns:
    True if string is palindrome, False otherwise
    """
    #Assuming that the given string is palindrome by setting (flag = True)
    flag = True
    #Setting backward pointer
    j = len(str) - 1
    for i in range(len(str)):
        #At any point if i exceeds j then return flag
        if i > j:
            return flag
        if str[i] == str[j]:
            #In each new iteration decrement the backward pointer
            j -= 1
        else:
            flag = False
    return flag


#Test the logic
str = input("Enter the string to check weather it is palindrome or not: ")
if is_palindrome(str):
    print(f"Given string '{str}' is a palindrome")
else:
    print(f"Given string '{str}' is not a palindrome")








#Problem 02: Fibonacci Series

def fibonacci_sequence(n):
    """
    Generate a fibonacci sequence of length n
    (0 1 1 2 3 5 8 13 21 ... )
    
    Args:
    n(int): length of fibonaaci squence to generate

    Returns:
    list: Fibonacci sequence of length n
    """
    fib_seq_list = []
    num1, num2 = 0, 1
    #Generate the fibonaaci squence
    for i in range(n):
        num3 = num1 + num2
        num1, num2 = num2, num3

        #Append the generated number to the list
        fib_seq_list.append(num1)
        
    return fib_seq_list


# Test the logic
fib_range = int(input("Enter the fibonacci sequence range: "))
fib_seq_list = fibonacci_sequence(fib_range)
print(f"Fibonacci sequence of length {fib_range} is: {fib_seq_list}")






# Problem 03: Anagram Detector
def is_anagram(str1, str2):
    """
    Check whether the two strings are anagrams or not

    Args:
    str1(str), str2(str): str1, str2 are the input strings

    Return:
    True if strings are anagrams else False
    """
    #Assume that the two strings are not Anagrams
    flag = False
    #Keep track of matched characters by setting count
    count = 0

    #Compute length of strings
    len_str1 = len(str1)
    len_str2 = len(str2)

    #If the length of two strings are not equal then, they are not anagrams
    if len_str1 != len_str2:
        return False
        
    #Check whether the two strings are anagrmas or not
    for i in range(len_str1):
        for j in range(len_str2):
            if str1[i] == str2[j]:
                #Keep track of matched characters
                count += 1
                #Set flag to True if there a match in any pass
                flag = True
        if not flag:
            return False
        #Reset flag to False, to ensure that there is no match in next pass
        flag = False

    #If count == length of str1 or str2, then str1 and str2 are anagrams
    if count == len_str1:
        return True
    else:
        return False
    


#Test the logic
print("Note: Strings are case sensative")
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
if is_anagram(str1, str2):
    print(f"Strings '{str1}' and  '{str2}' are ANAGRAMS")
else:
    print(f"Strings '{str1}' and  '{str2}' are NOT ANAGRAMS")






# Problem 04: Prime Number Checker
import math
def is_prime(num):
    """
    Check whether the given number is prime or not

    Args:
    num(int): num is the input number 

    Return:
    True if num is a prime number else False
    """

    #Handling the edge case
    if num == 1:
        return False
    #Check whether the given numbers (>=2) is prime or not
    for i in range(2, math.ceil(math.sqrt(num))):
        #If there is any divisor from 2 to square_root(given_number), then
        #For sure that number is not a prime number else Prime
        if num % i == 0:
            return False
    return True


### Test the logic
num = int(input("Enter the number: "))
if is_prime(num):
    print(f"Given number '{num}' is a PRIME NUMBER")
else:
    print(f"Given number '{num}' is  NOT a PRIME NUMBER")






#Problem 05: Word Frequency Counter
def word_freq_counter(str):
    """
    Given a string that consists of n words

    Args:
    str(str): Input string

    Return:
    frequecy of each word
    """

    #Split the strings into k words
    words = str.split()
    i = 0

    while i < len(words):
        #Creat a separate list that counts the frequency for each word
        frequiencie = [word for word in words  if words[i] == word]
        print(f"Word '{words[i]}' occurs: {len(frequiencie)} times")
        
        #Update list by removing encountered words
        words = [remaning_words for remaning_words in words if words[i] != remaning_words]
        
        #Reset the list to count the occurance of next word
        frequiencie = []
        i = 0
        
#Test the logic
sentance = input("Enter the string: ")
word_freq_counter(sentance)






#Problem 06: Binary To Decimal Conversion
def binary_to_decimal(num):
    """
    Convert the given binary number into decimal

    Args:
    num(str): num is the input binary number

    Return:
    Decimal number
    """
    #Initially keep sum of weights for a given binary number = 0
    sum_of_weights = 0
    
    #Assign weights to each bit
    for i in range(1, len(num) + 1):
        #Sum of weights
        sum_of_weights += int(num[-1*i]) * int(math.pow(2, i-1))  
    decimal_number = sum_of_weights
    
    return int(decimal_number)


#Test the logic
binary_number = input("Enter a valid binary number: ")
decimal_number = binary_to_decimal(binary_number)
print(f"The equivalent decimal number for the given binary number({binary_number}) is: '{decimal_number}'")






#Problem 07: Pattern Printing
#Right angled trinagle
def right_angled_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="  ")
        print("\n")
        

#Square
def square(rows):
    for i in range(rows):
        for j in range(rows):
            print("*", end="   ")
        print("\n")
        
#Triangle
def triangle(rows):
    for i in range(rows):
        #Print spaces to align starts
        for _ in range(rows - i - 1):
            print(" ", end=" ")
        #Print stars
        for _ in range(2 * i + 1):
            print("*", end=" ")
        print("\n")
        
#Inverted Triangle    
def inverted_triangle(rows):
    for i in range(rows):
        #Print spaces to align starts at their right position
        for _ in range(i):
            print(" ", end=" ")
        #Print stars
        for _ in range(2 * rows - 2 * i - 1):
            print("*", end=" ")
        print("\n")

#Dimond
def dimond(rows):
    #Print upper half of dimond (i,e upper triangle)
    triangle(rows // 2)
    #Print lower half of dimond (i,e inverted triangle)
    inverted_triangle(rows // 2)


import os
#Small Menu Deiven
choices = {
    1 : right_angled_triangle,
    2 : square,
    3 : triangle,
    4 : inverted_triangle,
    5 : dimond,
    6 : exit
}

while True:
    os.system("clear")
    print(f"{" " * 10} Shape Drawn")
    print("1. Print right angled triangle")
    print("2. Print square")
    print("3. Print triangle")
    print("4. Print inverted triangle")
    print("5. Print dimond")
    print("6. Exit")

    your_choice = int(input("Please enter a valid choice: "))
    if your_choice == 6:
        break
    choices[your_choice](int(input("Enter number of rows: ")))    
    





#Problem 08: Factorial Calculator
def factorial(num):
    """
    Calculate the factorial of a positive integer

    Args:
    num(int): Input integer

    Return:
    Integer value
    """

    #Handling edge case by setting zero factorial to 1
    fact = 1
    #Compute factorial
    for i in range(num):
        fact *= num - i

    return fact



# Test the logic
num = int(input("Enter a valid number: "))
print(f"The factorial of {num} is {factorial(num)}")





# Problem 09: String Reversal without builtin function 
def string_reverse(str):
    """
    Reverse the given string by swapping

    Args:
    str(str): Input string

    Return:
    Reverse of a string
    """
    rev_str = ""
    for i in range(len(str) - 1, -1, -1):
        #Concatenating the characters of 'str' with rev_str
        rev_str += str[i]

    return rev_str
    


#Test the logic
str = input("Enter the string: ")
print(f"The reverse of string '{str}' is '{string_reverse(str)}'")







# Problem 10: Sum of Digits Recursively
def sum_of_digits(num):
    """
    Compute sum of digits for a given number

    Args:
    num(int): Input number

    Return:
    Sum of digits
    """

    #Base case
    if num == 0:
        return 0
    return num % 10 + sum_of_digits(num // 10)



#Test the logic
num = int(input("Enter the number: "))
print(f"The sum of digits of the given number '{num}' is '{sum_of_digits(num)}'")






#Problem 11: Armstrong Number Checker
def is_armstrong(num):
    """
    Check whether the given number is armstrong or not

    Args:
    num(int): Input number

    Return:
    True if armstrong else False
    """

    #Assign orginal value to temp, and made necessary changes to temp
    temp = num
    sum = 0
    while temp:
        #Compute remainder
        rem = temp % 10
        
        #Compute sum of cubes of each digit
        sum += rem ** 3
        temp = temp // 10
    if sum == num:
        return True
    else:
        return False
        


#Test the logic
num = int(input("Enter a valid number: "))
if is_armstrong(num):
    print(f"Given number '{num}' is an armstrong number")
else:
    print(f"Given number '{num}' is NOT an armstrong number")
    
    




#Problem 12: Pascal's Triangle
#Compute factorial
def factorial(num):
    fact = 1
    for i in range(num):
        fact *= num - i

    return fact


#Compute nCr
def binomial_cofficient(n, r):
    #Compute value of binomial cofficient
    value = int(factorial(n) / (factorial(n - r) * factorial(r)))
    
    return value
        


def pascals_triangle(rows):
    """
    Display pascal's triangle upto given range

    Args:
    num(int): Input number

    Return:
    Displays pascals triangle
    """
    for i in range(rows):
        #Print spaces to align binomial cofficients
        for _ in range(rows - i - 1):
            print(" ", end="")
        #Append binomial cofficents at right places
        for j in range(i + 1):
            print(binomial_cofficient(i, j), end=" ")

        print("\r") 


rows = int(input("Enter number of rows: "))
pascals_triangle(rows)





