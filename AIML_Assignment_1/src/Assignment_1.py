

"""
Artificial Intelligence and Data Science
Assignment 02
"""



#Problem 01: ARITHMETIC OPERATIONS<

#Define operations using lambdas
operations = {
    "add": lambda x, y: (x + y),
    "subtract": lambda x, y: (x - y),
    "multiply": lambda x, y: (x * y),
    "divide": lambda x, y:  round((x / y), 2)
}

#Function to perform on selected operation
def calculator(num1, num2, operation):
    operation_fun = operations.get(operation)

    #Return result of operation
    return operation_fun(num1, num2)

#Function to select the operation
def select_operation():
    while True:
        print("Enter any of the below operation")
        print(" 👉 add")
        print(" 👉 subtract")
        print(" 👉 multiply")
        print(" 👉 divide")

        return input("Enter operation: ")




# Test the logic
num1 = float(input("Enter ist number: "))
num2 = float(input("Enter 2nd number: "))

#Select operation
operation_selected = select_operation()
print(f"The {operation_selected} operation of given two numbers is: {calculator(num1, num2, operation_selected)}")








#Problem 02: ARITHMETIC OPERATIONS CONTINUED

#Function to perform addition
def add(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
    

#Function to perform multiplication
def multiply(nums):
    mul = 1
    for num in nums:
        mul *= num
    return round(mul, 2)


#Define operations using functions
operations = {
    "add": add,
    "multiply": multiply
}

#Function to perform on selected operation(variable len arguments)
def calculator(operation, *nums):
    return operations.get(operation)(nums)


#Function to select the operation
def select_operation():
    while True:
        print("Enter any of the below operation")
        print(" 👉 add")
        print(" 👉 multiply")

        return input("Enter operation: ")



#Test the logic
#Select operation
operation_selected = select_operation()

#Variable length arguments
result = calculator(operation_selected, 1, 2, 3, 4, 3.2)
print(f"Result of {operation_selected} operation is : {result}")



#Function to perform addition
def add(nums):
    sum = 0
    for key, value in nums.items():
        sum += value
    return sum
    
#Function to perform multiplication
def multiply(nums):
    mul = 1
    for key, value in nums.items():
        mul *= value
    return round(mul, 2)



#Define operations using functions
operations = {
    "add": add,
    "multiply": multiply
}     
        
#Function to perform on selected operation(keyword variable len arguments)
def calculator(operation, **kwargs):
    return operations.get(operation)(kwargs)



#Test the logic
#Select operation
operation_selected = select_operation()

#keyword arguments
result = calculator(operation=operation_selected, num1=2, num2=30, num3=90)
print(f"Result of {operation_selected} operation is : {result}")








#Problem 03: PLAYING WITH STRINGS

#Function to select the operation
def select_operation():
    while True:
        print("Enter any of the below operation")
        print(" 👉 concatenation")
        print(" 👉 1")
        print(" 👉 i")

        return input("Enter operation: ")
        

#Function to perform string concatenation
def concatenation(args):
    new_string = ""
    for arg in args:
        new_string += arg
        
    return new_string

#Function to perfrom string concatenation by taking first character of each string
def concatenate_initials(args):
    new_string = ""
    for arg in args:
        new_string += arg[0]

    return new_string
    

#Function to perfrom concatenation by taking i character of each string
def concatenate_ith_character(i, args):
    #Assume that each string does not contain the ith character by setting (flag to False).
    flag = False
    new_string = ""
    
    for arg in args:
        if i < len(arg):
            new_string += arg[i]
            flag = True
            
    if flag:
        return new_string
    else:
        return "No String Found🙃"   


#Define operations
operations = {
    "concatenation": concatenation,
    "1": concatenate_initials,
    "i": concatenate_ith_character
}


#Runner
def runner(*args, operation, i=None):
    if i == None:
        return operations.get(operation)(args)
    else:
        return operations.get(operation)(i, args)


#Test the logic
operation_selected = select_operation()

if operation_selected in ["concatenation", "1"]:
    result = runner("Zakir", "Rashid", "Mir", "Kupwara", operation=operation_selected)
else:
    index = int(input("Please Enter the value of ith index: "))
    result = runner("Zakir", "Rashid", "Mir", "Kupwara", operation=operation_selected, i=index)

print(f"Final Result: {result}")





#Problem 04: PLAYING WITH STRINGS AGAIN 
def is_present(str1, sub):

    #Compute lengths of each string
    len1 = len(sub)
    len2 = len(str1)

    #Set both the pointers to the first indicies
    i = j = 0
    while i < len1 and j < len2:
        while j < len2:
            if sub[i] == str1[j]:
                i += 1
                j += 1
                break
            else:
                #If there is no match for the first character of sub, then
                #set sub pointer to first index, in order to check its firsrt character with
                #k character of str
                i = 0
                j += 1

    #Check if i traverse the whole substring
    if i == len1:
        return True
    else:
        return False


#Test the logic
string = input("Enter first string: ")
sub = input("Enter second string: ")

if is_present(string, sub):
    print(f"Sub string '{sub}' is present in '{string}'")
else:
    print(f"String '{sub}' is NOT present in '{string}'")
    
    






#Problem 05: DIVIDE STRINGS
def divide_string(str1):
    part1 = ""
    part2 = ""

    #Convert string into list of characters
    str_list = [char for char in str1]

    for i in range(len(str_list)):
        if (i % 2 == 0 or i % 3 == 0) and i % 6 != 0:
            part1 += str_list[i]
        else:
            part2 += str_list[i]

    return part1, part2



#Test the logic
str1 = input("Enter the string: ")
part1, part2 = divide_string(str1)

print(f"\nPart of string that's divisible by 2 or 3 but not both is : '{part1}'")
print(f"Rest part of string: '{part2}'")






#Problem 06: PRINTING SERIES

import math
#Generate fibonacci sequence
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


#Generate multiples of given number   
def multiples_of_series(series, bound):
    """
    Generate multiples of series
    
    Args:
    int(series): series is an integer whome which we have to calculate multiples
    int(bound): calculate multiples upto certain range, given by bound

    Returns:
    list: multiples of series
    """
    #Compute multiples of series
    multiples = [x * series for x in range(1, bound + 1)]
    return multiples


    
#Generate frist B odd integers
def ist_b_odd_integers(bound):
    odd_integers = [x for x in range(1, 2 * bound + 1) if x % 2 != 0]
    return odd_integers



#Generate first B prime numbers
def ist_b_prime_numbers(bound):
    #Store prime numbers
    prime_numbers = [2]
    #Check from number 3, and move onwards
    num = 3
    #Keep track of count of prime numbers
    count = 0
    
    while True:
        #Assume that the number is prime by setting (flag = True)
        flag = True
        
        #If count == bound, then our requirement is fullfilled, hence break        
        if count == bound:
            break
        
        #Check weather 'num' is a prime number or not if so, then append to prime_number list
        for i in range(2, math.ceil(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            count += 1
            prime_numbers.append(num)

        #Increment number by 1
        num += 1
       
    return prime_numbers
            
        
    

#Check for series type
def series_type(bound, series):
    if series == "fibonacci":
        return fibonacci_sequence(bound)
    elif series == "8":
        return multiples_of_series(int(series), bound)
    elif series == "odd":
        return ist_b_odd_integers(bound)
    elif series == "prime":
        return ist_b_prime_numbers(bound)
    

list_sequence_number = []
#Return list of number sequence
def printing_series(bound, series, otype=None):
    global list_sequence_number

    #Store all the generated numbers into list_sequence_number list
    list_sequence_number += series_type(bound, series)
    



#Test the logic
bound = int(input("Enter bound: "))


printing_series(bound, series="fibonacci")
printing_series(bound, series="8")
printing_series(bound, series="odd")
printing_series(bound, series="prime")

print(f"Required list sequence\n{list_sequence_number}")







#Problem 07: RESEARCH ON STRING </i>

#Research on methods of strings
string = "zakir rashid"
print(f"String Methods and Properties {dir(string)}")


#Method 01: Capitalize 
#Capitalize method
"""
This method will help us to capitalize the first character of the string

Arg:
This method doen't take any argument

Return:
This 'll return a new string (capitalize string)
"""
new_string = string.capitalize()
print(f"Captilized string: {new_string}")



#Method 02: Casefold </li>
#Casefold method
"""
This method will help us to convert a string into lower case string.
This is same as lower(), but the only difference is that casefold is more
aggressive, that's it has the additional capability to convert unicode characters into
lower case, which lower() method can't do

Arg:
This method doen't take any argument

Return:
This 'll return a new string (casefolded  string)
"""
new_string = string.casefold()
print(f"Casefolded string: {new_string}")


#Method 03: Center </li>
#center method
"""
This method will help us to center a string on console. It uses
the given width and assigns width to the string required to it.
And the remaning width is equially distributed on left and right side,
by default empty space is not filled with anything

Args:
width(int): Integer width
fillerchar(str): Used to fill the remaing space

Return:
This 'll return a new string (centered  string)
"""
new_string = string.center(30, "~")
print(f"Centered string: {new_string}")


#Method 04: Count
#count method

"""
This method will help us to center a string on console. It uses
the given width and assigns width to the string required to it.
And the remaning width is equially distributed on left and right side,
by default empty space is not filled with anything

Args:
width(int): Integer width
fillerchar(str): Used to fill the remaing space

Return:
This 'll return a new string (centered  string)
"""
new_string = string.center(30, "~")
print(f"Centered string: {new_string}")


#Method 05: Endwith
#Endwith method

"""
This method checks whether a strings end with a given suffix or not.
If it ends with a given suffix, then it returns True else False

Args:
suffix(str): Input string

Return:
True or False
"""

suffix = "id"
yes_no = string.endswith(suffix)

if yes_no:
    print(f"The strings {string} ends with given suffix '{suffix}'")
else:
    print(f"The strings {string} DOES NOT ends with given suffix '{suffix}'")
    
    

#Method 06: Find
#Find Method

"""
This method is used to find the index of the substring,
if the substring is present it it'll return the index of the
first character else i'll return -1

Args:
sub(str): Input sub string

Return:
index(int): if found then return index else return -1 
"""

sub = "ras"
index = string.find(sub)

if index != -1:
    print(f"Sub string '{sub}' is present in string {string}")
else:
    print(f"Sub string '{sub}' is NOT present in string {string}")


#Method 07: Format 
#Format Method


"""
This method is used to format the string, by replacing
the curcly braces with the actual content based on whether we 
are passing variable number of positional arguments, or key word
arguments.

Args:
str(*args, **kwargs)

Return:
str(string): Formatted string
"""

#String formatting using only positional arguments
string = "Hello {} of  Milky way {}"
print("Formatted string is: ", string.format("Alien's", "Glaxy"))

#String formatting using only keyword arguments
aliens = "Alien's"
glaxy = "Glaxy"
string = "Hello {aliens} of  Milky way {glaxy}"
print("Formatted string is: ", string.format(aliens=aliens, glaxy=glaxy))


#Method 08: Split
#Split Method

"""
This method splits the string based on given separator,
if no separator is given then by default empy sapce is taken
as a separator

Args:
str(sep): sep is the given separator
maxsplit(int): Signifies maximum words that needs to be split

Return:
str(list): Retuns list of string
"""

string = "Zack is about to reach home Zack"
spl_string = string.split(sep=" ", maxsplit=3)
print(f"Splitted string is: {spl_string}")


#Method 09: Replace
#Replace Method


"""
This method is used to replace a 'word' with another 'word'
and returns a new string

Args:
str(old): old word that needs to be replaced
str(new): new word which replaces old word
int(count): replace 'count' number of occurance

Return:
str(new_str): retuns new string
"""

old_string =  "Zack is about to reach home Zack"
new_string = old_string.replace("Zack", "xack")
print(f"New string is:  {new_string}")


#Method 10: Strip
#Strip Method


"""
This method is used to remove the same starting and ending
of characters if they are same.
It quite often used to remove the white spaces before and after
the string

Args:
str(chars): Optional argument

Return:
str(new_string): Returns a new string
"""
string = "    Zack is coding!!!   "
print(f"String before strip: {string}")
print(f"Stripped string is: {string.strip()}")









#Problem 8: MANIPULATING THE TYPE
import math

#Generate fibonacci sequence
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


#Generate multiples of given number   
def multiples_of_series(series, bound):
    """
    Generate multiples of series
    
    Args:
    int(series): series is an integer whome which we have to calculate multiples
    int(bound): calculate multiples upto certain range, given by bound

    Returns:
    list: multiples of series
    """
    #Compute multiples of series
    multiples = [x * series for x in range(1, bound + 1)]
    return multiples


    
#Generate frist B odd integers
def ist_b_odd_integers(bound):
    odd_integers = [x for x in range(1, 2 * bound + 1) if x % 2 != 0]
    return odd_integers



#Generate first B prime numbers
def ist_b_prime_numbers(bound):
    #Store prime numbers
    prime_numbers = [2]
    #Check from number 3, and move onwards
    num = 3
    #Keep track of count of prime numbers
    count = 0
    
    while True:
        #Assume that the number is prime by setting (flag = True)
        flag = True
        
        #If count == bound, then our requirement is fullfilled, hence break        
        if count == bound:
            break
        
        #Check weather 'num' is a prime number or not if prime, then append to prime_number list
        for i in range(2, math.ceil(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            count += 1
            prime_numbers.append(num)

        #Increment number by 1
        num += 1

    return prime_numbers
            

#Check for series type
def series_type(bound, series):
    if series == "fibonacci":
        return fibonacci_sequence(bound)
    elif series == "8":
        return multiples_of_series(int(series), bound)
    elif series == "odd":
        return ist_b_odd_integers(bound)
    elif series == "prime":
        return ist_b_prime_numbers(bound)


#Convert numbers into letters
def number_to_letters(number_list):
    #Number to letter mapping
    mapping = {i: chr(i + 65) for i in range(0, 26)}

    return [mapping[num % 26] for num in number_list]
    


#Convert decimal numbers to octal numbers
def decimal_to_octal(number_list):
    octal_number_list = []

    #Convert decimal into octal
    for dec in number_list:
        rev_octal_number = 0

        #This loops converts decimal into octal but gives reverse order of octal number
        #E.g dec(115) = oct(163), but this loops gives 361
        while dec >= 1:
            rem = dec % 8
            rev_octal_number = rev_octal_number * 10 + rem
            dec //= 8
            

        #Reverse the octal number
        octal_number = 0
        while rev_octal_number >= 1:
            rem = rev_octal_number % 10
            octal_number = octal_number * 10 + rem
            rev_octal_number //= 10

        octal_number_list.append(octal_number)   

    return octal_number_list



#Hexa mapping function
def hexa_mapping(rem):
    #Create a mapping b/w integers from 10 to 15, with their correspoind character values
    mapping = {i: chr(55 + i) for i in range(10, 16)}
    return mapping[rem]

    


#Convert decimal numbers to hexa-decimal numbers
def decimal_to_hexa(number_list):
    hexa_number_list = []

    #Convert decimal into hexa
    for dec in number_list:
        rev_hexa_number = ""

        #This loops converts decimal into hexa-decimal but gives reverse order of hexa-decimal number
        #E.g dec(115) = hexa(73), but this loops gives 37
        while dec >= 1:
            rem = dec % 16
            if rem in [10, 11, 12, 13, 14, 15]:
                rem = hexa_mapping(rem)
            rev_hexa_number += str(rem)
            dec //= 16
            

        #Reverse the hexa-decmial number
        hexa_number = rev_hexa_number[::-1]
        hexa_number_list.append(hexa_number)   

    return hexa_number_list


#Convert decimal number into binary
def dec_to_bin(nums):
    bin_number_list = []

    #Do conversion
    for num in nums:
        bin = ""   
        while num > 0:
            rem = num % 2
            num //= 2
            bin += str(rem)
        #Do reverse of binary number and append it to the list
        bin_number_list.append(bin[::-1])

    return bin_number_list
        

list_sequence_number = []
#Return list of number sequence
def printing_series(bound, series, otype=None):
    global list_sequence_number

    #If otype is not specified, then compute simply list sequence number
    if otype == None:
        list_sequence_number += series_type(bound, series)

    if otype == "letter":
        #Convert list sequence numbers into letters (Encoding)
        return number_to_letters(list_sequence_number)
    elif otype == "oct":
        #Convert decmial numbers list into octal numbers
        return decimal_to_octal(list_sequence_number)
    elif otype == "hex":
        #Convert decimal numbers list into hexa numbers
        return decimal_to_hexa(list_sequence_number)
    elif otype == "bin":
        #Convert decimal number list into binary
        return dec_to_bin(list_sequence_number)


def select_otype():
    while True:
        print("Enter any of the below operation")
        print(" 👉 letter")
        print(" 👉 oct")
        print(" 👉 hex")
        print(" 👉 bin")

        return input("Enter operation: ")

    

#Test logic
bound = 10
#Compute list number sequence
printing_series(bound, series="fibonacci")
printing_series(bound, series="8")
printing_series(bound, series="odd")
printing_series(bound, series="prime")

print(f"List Number Sequence\n{list_sequence_number}")

#Compute conversion of number list (endcoding, oct, hex, bin)
conversion_list = printing_series(bound, series="", otype=select_otype())
print(f"Encoding of ABOVE 'NUMBER' list is\n {conversion_list}")









#Problem 09: TUPLES AND DICTIONARIES 

#Research on tuples
#Tuples are immutable, ordered and can contain duplicate elements
my_tuple = (1, 2, 3, 4, 5, 6, 9)
print(dir(my_tuple))


#Method 01: Add

"""
This method is used to add the elements of two or more tuples,
this method is internally invoked when we call
+ operator b/w tuples
"""
names = ("Zakir", "Sohai", "Musaib")
ages = (22, 23, 232)

#Add two tuples 
names_ages = names + ages
print(f"New tuple: {names_ages}")


#Method 02: Contains
"""
This method is used to know whether an element belongs
to the tuple or not. This methods gets invoked when we
place in operator b/w an element and tuple
"""

my_tuple = ("Zack", "Rashid", "Mir")

if "Zack" in my_tuple:
    print(f"Yes 'Zack' belongs to {my_tuple}")
else:
    print(f"No 'Zack' DOES NOT belongs to {my_tuple}")


#Method 03: Eq
"""
This method is used to check whether the two tuples
are equal or not, this method gets invoked when it encounters
== in b/w tuples
"""

tuple1 = ((1, 2, 2), (1, 19, 2))
tuple2 = ((1, 2, 2), (1, 19, 2))

if tuple1 == tuple2:
    print(f"The two tuples are equal")
else:
    print(f"The two tuples are NOT equal")



#Method 04: Getitem
"""
This method is used to get an element from tuple.
It gets invoked when [] are used with tuple 
"""
tuple1 = ((1, 2, 2), (1, 19, 2))
print(f"Element at '[0][1]' location is: {tuple1[0][1]}")


#Method 05: Iter
#This method is used to make tuple iterable
nums = ("Zakir", 22, "Sohail", 33)
for num in nums:
    print(num, end = " ")


#Method 06: Len
#This method is used to get the length of a list
nums = ("Zakir", 22, "Sohail", 33)
print(f"Length of above list is: {len(nums)}")


#Method 07: Repr
#This method is used to get the string representation of tuple
my_tuple = (1, 2, 3, 4)
str_tuple = repr(my_tuple)
print(f"String representation of above tuple is: {str_tuple}")
print(f"Class of 'str_tuple' is: {type(str_tuple)}")


#Method 08: Str 
#This method returns the human redable string format of tuple
my_tuple = (1, 2, 3, 4)
print(f"String represenation of above tuple is: {str(my_tuple)}")
print(f"Class of 'str_tuple' is: {type(str_tuple)}")
print(str(my_tuple))


#Method 09: Mul </li>
#This method is used to increase the langth of an array
#by integer multiple times. 
#Note: It doesn't perform arithmetic operation to the elements of an array

nums = (1, "Zack", "Ali", (1, 2, 3))
print(f"After multiplying by 5: {nums * 3}")



#Method 10: Index
#This method is used to get the index of an element within the tuple
nums = ("Cs", "Ce", "Me")
print(f"'Ce' is stored at index: {nums.index("Ce")}")




#Research on dictionary
#Dictionaries are ordered, changable and do not allow duplicates
dic = {
    "name": "Zakir",
    "age": 23,
    "major": "cse"
}
#Properties and Methods of dictionaries
print(dir(dic))


#Method 01: Clear
#This method is used to clear/delete all the key value paris
dic.clear()
dic

#Method 02: Copy
#This method returns 'Shallow copy' of dictionary.
#'Shallow Copy': Changes made to shallow copy won't affect the orginal dict

dic = {
    "name": "Zakir",
    "age": 23,
    "major": "cse"
}

#Create a shallow copy
shallow_copy = dic.copy()
print(f"Shallow Copy {shallow_copy}")


#Method 03: FromKeys 

#This method is used to create a new dict, in which
#keys are same as of old dict and values are different

old_dict = {
    "name": "Zakir",
    "age": 23,
    "major": "cse"
}

old_dict_keys = ("name", "age", "major")

#Creating new dictionary with same keys and values 'None'
new_dict = dict.fromkeys(old_dict_keys, None)
print(f"New dict with default values: {new_dict}")


new_values = ["Xack", 29, "AIML"]
#New dict with new values and same keys
#Using dict comprehension
new_dict = {key: new_values.pop(0) for key in list(old_dict.keys())}
print(f"New dict with new values: {new_dict}")

#Method 04: Get
#This method returns the value of a given key
print(f"Value of key 'name' in 'new_dict' is: {new_dict.get("name")}")


#Method 05: Items
#This method provides a view of dictionary items
print(f"View of 'new_dict' is: {new_dict.items()}")

#Method 06: Keys
#This method provides a view on dictionary keys
print(f"View on dictionary keys is: {new_dict.keys()}")

#Method 07: Pop 
"""
This method is used to remove the key value pair, if
the key is not found then return default and if default
is not specified then raise KeyError

Args:
(key, [,default]): default is optional

Return:
Value associated to given key
"""

dict_copy = new_dict.copy()
#Remove this key value pair 'name: Zack' 

dict_copy.pop("name")
print(f"New state of dict_copy is: {dict_copy}")
dict_copy.pop("dob", "no such key found")


#Method 08: Popitem
#This method is used to get and remove the last entered key value pair
new_dictx = new_dict.copy()
print(f"Removing in LIFO order {new_dictx.popitem()}")
print(f"New state of 'new_dictx' is: {new_dictx}")









#Problem 10: STATISTICS
import math
#Compute mean
def compute_mean(args):
    sum = 0
    for arg in args:
        sum += arg
    return sum/len(args)


#Compute variance
def compute_variance(args):
    mean_value = compute_mean(args)
    sum = 0
    for arg in args:
        sum += (arg - mean_value) ** 2

    #Calculate variance
    var_ = sum / len(args)

    return var_


#Compute SD
def compute_sd(args):
    return round(math.sqrt(compute_variance(args)), 3)


#Compute statistics (Mean and SD)
def statistics(*args, quantity):
    if quantity == "mean":
        return compute_mean(args)
    elif quantity == "sd":
        return compute_sd(args)

def select_statistic_operation():
    while True:
        print("Enter any of the below operation")
        print(" 👉 mean")
        print(" 👉 sd")

        return input("Enter operation: ")

#Test the logic
result = statistics(1, 2, 39, 4, quantity=select_statistic_operation())
print(f"Result of above statistic operation is:  {result}")










#Compute sum of digits
def sum_of_digits(num):
    sum = 0
    while num >= 1:
        sum += num % 10
        num //= 10

    return sum

#Function that will return indicies of elements thare are divisible by 3
def divisible_by_3(nums):
    #Nested function to check which element is divisibel by three
    def is_divisible_by_3(num):
        return sum_of_digits(num) % 3 == 0

    #Store indices of those elements which are divisible by 3
    indices = []
    for index, num in enumerate(nums):
        if is_divisible_by_3(num):
            indices.append(index)

    return indices



#Function that'll return an array consists of any power of array elements
def any_power(nums, pow):
    return [num ** pow for num in nums]


#Function that'll check for sixth power of given element 'number'
def check_sixth_power(nums, pow, number):
    power_arry = any_power(nums, pow)
    
    #Nested function will check whether sixth power of some number is present in power_arry or not
    def is_sixth_power_present(number):
        for num in power_arry:
            if num == number:
                return True
        return False

    #Return True if sixth power is present
    if is_sixth_power_present(number):
        return True
    
    return False


def select_operation():
    while True:
        print("Enter any of the below operation")
        print(" 👉 divisible")
        print(" 👉 sixth-power")

        return input("Enter operation: ")


#Test the logic
nums = [1, 2, 9, 11, 12, 89, 7, 3, 0]
pow = 3
operation_selected = select_operation()

if operation_selected == "divisible":
    print(f"List of indicies of elements that are divisibel by 3 \n{divisible_by_3(nums)}")
elif operation_selected == "sixth-power":
    num = int(input("Enter number to check it's sixth power: "))
    if check_sixth_power(nums, pow, num):
        print(f"Sixth power of {num} is present")
    else:
        print(f"Sixth power of {num} is NOT present")








#Problem 12: LAMBDA FUNCTIONS
#Function that'll check if the two arrays are same or not
def are_same_arrays(nums1, nums2):
    #Create an array that'll contain True on places where the elements
    #are same otherwise False
    boolean_result = list(map(lambda x, y: True if x == y else False, nums1, nums2))

    #Now i'll check if there is any false in 'boolean_result' if it contains, then clearly
    #it mean that the two arrays are not same
    are_same = list(filter(lambda x: x is False, boolean_result))

    #If the len(are_same) list is 0, then two arrays are same else not
    return len(are_same) == 0

#Function that'll create an array that contains same number of zeros as 'nums' does
def same_no_of_zeros(nums):
    return list(map(lambda x: x * 0, nums))

#Are two arrays same
nums1 = [1, 2, 3, 99, 10, 11]
nums2 = [10, 20, 30, 50, 110]

if are_same_arrays(nums1, nums2):
    print(f"The Given two arrays are same")
else:
    print(f"The Given two arrays are NOT same")
    
#New array that contains as many zeros as len(nums)
nums = [x for x in range(1, 100, 2)]
print(f"Zero array corresponding to 'nums' array is:\n{same_no_of_zeros(nums)}")


#Problem 13: SHORT BUT STRONG
import math
#Function that'll compute value of e^x cos(x)
def exponential_trigonomertic(nums):
    output = []
    for num in nums:
        #Compute value of e^num
        expo = math.pow(math.e, num)
        
        #Compute value of cos(num)
        tri = math.cos(num)

        #Compute and store output
        output.append(round(expo * tri, 2))

    return output
    

#Test the logic
n = int(input("Enter value of n (2) (Caution: OVERFLOW MAY OCCUR FOR LARGE VALUES OF N)"))
#Compute 9 power n
nine_power_n = int(math.pow(9, n))

#Create a list from 1 to 9 power n
nums = [num for num in range(1, nine_power_n)]

print(f"Output of above mathematical equation is: \n {exponential_trigonomertic(nums)}")











#Problem 14: REVERSE SORT
#Performing insertion sort
def sort_in_dec_order(nums):
    """
    This function will pick the element (key) from unsorted array and 'll
    place the element in sorted array

    Args: 
    list(nums): Unsorted array

    Return:
    list(nums): sorted array
    """
    
    for i in range(1, len(nums)):
        #Pick key element (starting from second element)
        key = nums[i]
        j = i - 1

        while j >= 0:
            if key > nums[j]:
                nums[j + 1] = nums[j]
            else:
                break
            j -= 1
        #Place key element at its right position
        nums[j + 1] = key

    print(nums)


#Test the logic
nums = [1, 2, 9, -2, 0]
sort_in_dec_order(nums)
print(f"Sorted array in decreasing order is: {nums}")

#Sort using builtin function 'sorted'
sorted(nums, reverse=True)







#Problem 15: UNEXPECTED RETURN

#Function with abrupt return
def first_occur_of_0(nums):
    for index, num in enumerate(nums):
        if num == 0:
            return index #Abrupt return if 0 is encountered

#Function with break
def first_occur_of_0_using_break(nums):
    for index, num in enumerate(nums):
        if num == 0:
            break #Break if condition is met
    return index
            
# 
# <h4 style="color: green"> The difference b/w above two function is:</h4>
# 
# first_occur_of_0:  This function will stop the execution the moment condition is met, 
# and nothing after return statement is hit will be executed
# first_occur_of_0_using_break:  This function will also execute the statements that are
#     after the for loop, only halts execution of loop when condition is met
# 



#Test the logic
nums = [1, 2, 3, 99, -4, 0, 4, 0, 2, 2, 44, 88]
print(f"First occurance of '0' using abrupt return is at index: {first_occur_of_0(nums)}")
print(f"First occurance of '0' using break is at index: {first_occur_of_0_using_break(nums)}")
