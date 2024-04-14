


#Assignment 02 
#Numpy(Numerical Python)

import numpy as np
import pandas as pd


#Problem 01:  MANIPULATING EXISTING ARRAYS

#1.1 Load from a txt file
#Load breast cancer data from data.txt
bcancer_data = np.loadtxt("../Data_set/data.txt", skiprows=1)
bcancer_data


#1.2 Load from csv file
#Load salaries data from salaries.csv file
salaries = np.loadtxt("../Data_set/salaries.csv", delimiter=",")
salaries


#1.3 Make a list into an array
#Function thal'll convert list into numpy arrary

def list_to_numpy_array(arr, flag):
    """
    Convert list into numpy array

    Parameters:
    arr(list), flag(str): Input matrix and flag respectivelly

    Return:
    arr(numpy.ndim): output array
    """
    return np.array(arr, dtype=flag)
    

numpy_array = list_to_numpy_array([1, 200.98, 3, 4], "float64")
print(f"Returned numpy array is: {numpy_array}")








#Problem 02:  MAKING ARRAY FROM SCRATCH

#2.1 Making Block diagonal arrays
#Function that'll generate a random 3 x 3 (int) matrices
rng = np.random.default_rng()
def matrices_ceator():
    """
    Create a random 3 x 3 matrix

    Parameter:
    None

    Return:
    arr(numpy.ndim): output array
    """
    return rng.integers(2, 8, size=(3, 3), endpoint=True)

mat1 = matrices_ceator()
mat2 = matrices_ceator()
mat3 = matrices_ceator()

#Create a block matrix
block_mat = np.block([
    [mat1, np.zeros(18).reshape(3, 6)],
    [np.zeros(9).reshape(3, 3), mat2, np.zeros(9).reshape(3, 3)],
    [np.zeros(18).reshape(3, 6), mat3]
])

#Print block matrix
print(f"Block Matrix is:")
block_mat



#2.2 Off diagonal block matrix
#Create an off diagonal block matrix
off_diag_block_mat = np.block([
    [np.zeros(9).reshape(3, 3), mat1, np.zeros(9).reshape(3, 3)],
    [mat2, np.zeros(18).reshape(3, 6)],
    [np.zeros(9).reshape(3, 3), mat3, np.zeros(9).reshape(3, 3)]
])

#Print off diagonal block matrix
print("Off diagonal block matrix is:")
off_diag_block_mat




#2.4 Matrix Operations
#Function that'll check whether the given matrix is symmertic or not
def is_symmetric(mat):
    """
    Check if the given matrix is symmertic or not

    Parameter:
    mat(array.ndim): Input numpy array

    Return:
    bool: return True if the given matrix is symmetric otherwise False
    """
    return True if np.array_equal(arr, arr.T) else False


#Function that'll check whether the given matrix is anti-symmetric or not
def is_anti_symmetric(mat):
    """
    Check if the given matrix is anti-symmetric or not

    Parameter:
    mat(array.ndim): Input numpy array

    Return:
    bool: return True if the given matrix is anti-symmetric otherwise False
    """
    #Check if arr + arr.T = 0, then return True else return False
    return True if np.all(arr + arr.T == 0) else False



#Function that'll check whether the given matrix is idempotent or not
def is_idempotent(mat):
    """
    Check if the given matrix is idempotent or not

    Parameter:
    mat(array.ndim): Input numpy array

    Return:
    bool: return True if the given matrix is idempotent otherwise False
    """
    return True if np.array_equal(mat * mat, mat) else False



#Function that'll check whether the given matrix is hermitian or not
def is_hermitian(mat):
    """
    Check if the given matrix is hermitian or not

    Parameter:
    mat(array.ndim): Input numpy array

    Return:
    bool: return True if the given matrix is hermitian otherwise False
    """
    return np.allclose(mat, np.conjugate(mat.T))


#Function that'll check whether the given matrix is unitary or not
def is_unitary(mat):
    """
    Check if the given matrix is unitary or not

    Parameter:
    mat(array.ndim): Input numpy array

    Return:
    bool: return True if the given matrix is unitary otherwise False
    """

    product = np.dot(mat, np.conjugate(mat.T))
    return np.allclose(product, np.eye(mat.shape[0]))

#Select Operation
operation = {
    "symmetric": is_symmetric,
    "anti-symmetric": is_anti_symmetric,
    "idempotent": is_idempotent,
    "hermitian": is_hermitian,
    "unitary": is_unitary
}


#Select operation
def select_operation():
    while True:
        print("Set of operations (select any one)")
        print("👉➤ symmetric")
        print("👉➤ anti-symmetric")
        print("👉➤ idempotent")
        print("👉➤ hermitian")
        print("👉➤ unitary")
        
        return input("Select 'Flag' value: ")
        

#Check type of matrices
def check_type(mat, flag):
    if flag not in operation.keys():
        return "Invalid Operation"
    #If flag value is valid then call an appropiate function
    return operation.get(flag)(mat)


#Complex square matrix
arr = np.array([
    [3j / np.sqrt(2), -1 / np.sqrt(2)],
    [1 / np.sqrt(2), -1j / np.sqrt(2)]   
])

#Select operation
op = select_operation()
if check_type(arr, op):
    print(f"Given matrix is {op} matrix")
else:
    print(f"Given matrix is not a {op} matrix")
    



#2.5 Array Operations
#Function that'll convert a given 1D array into 2D array
def _1D_to_2D(arr):
    """
    Convert a given 1D array into 2D array(matrix)

    Parameter:
    arr(array.ndim): Input 1D array

    Return:
    arr(array.ndim): Ouput 2D array(matrix)
    """

    return np.reshape(arr, (3, arr.shape[0]//3))

#Create a vector of size 18
arr = np.random.randint(2, 15, 18)

#Convert it into 2D array
print("After converting into 2D array")
_1D_to_2D(arr)




#2.6 Avoiding element-wise comparison
#Function that'll check whether the elements at 3i position are same or not
def comparasion_using_all(arr):
    """
    Check elements at 3i position

    Parameters:
    arr(array.ndim): Input 1D array

    Return:
    bool: True if they are same otherwise False
    """
    
    #Extract elements at position 3*n (n belongs to Z) Using slicing
    extracted_arr = arr[::3]
    
    #Compare all the elements of extracted_arr, if same then return True otherwise False
    return np.all(extracted_arr == extracted_arr[0])


#Input array
arr = np.array([
    11, 2, 3, 11, 21, 34, 11, 239
])

if comparasion_using_all(arr):
    print(f"The elements of given array are same at '3i' positions")
else:
    print(f"The elements of given array are not same at '3i' positions")









#Problem 03:  EXPONENTIALS

#3.1 Exponentials
import math
#Function that'll compute exponential of given matrix using taylor expansion
def taylor_expansion(mat):
    """
    Compute taylor expansion upto 3rd power

    Parameter:
    mat(array.ndim): Input matrix

    Return:
    array.ndim: Output matrix that contains exponential values
    """
    #Taylor expansion formula upto 3rd power
    taylor_formula = lambda x: 1 + x + (np.square(x) / math.factorial(2)) + ((x**3) / math.factorial(3))

    #Compute exponential values Create an empy matrix of same shape(like mat)
    exponent_values = np.empty_like(mat, dtype=float)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            #Append values at their right positions
            exponent_values[i, j] = taylor_formula(mat[i, j])

    #Return exponential value matrix
    return exponent_values

print(f"Value of exponentials using 'Taylor Expansion' is:\n {taylor_expansion(np.array([[1, 2, 3], [8, 9, 10]]))}")
print(f"Value of exponentials using 'Numpy Function' is:\n {np.exp(np.array([[1, 2, 3], [8, 9, 10]]))}")


# Reason for not being same
#The two exponential values are not same, because we are only computing taylor serires upto
#third power, which eventually looses precesion, hence gives inaccurate results





#3.2 Euler’s formula
#Function that'll validate Euler formula
#e^ix = cos(x) + jsin(x)
def validate_euler_formula(mat):
    """
    Validate eulers formula

    Parameter:
    mat(array.ndim): Given input matrix

    Return:
    bool: True if the computed values are same otherwise False
    """

    #Compute exponential values of mat (i,e e^(ix))
    e_power_iota_mat = np.exp(mat * 1j)
    
    #Compute cos(mat) and sin(mat)
    cos_mat = np.cos(mat)
    sin_mat = np.sin(mat)

    #Return True if they are same otherwise False
    return np.allclose(e_power_iota_mat, cos_mat + 1j * sin_mat)

#Create a random 3 x 3 integer matrix 
mat = np.random.randint(9, size=(3, 3))
if validate_euler_formula(mat):
    print("Eulers formula validated 🥰")
else:
    print("Something bad happen:(😣⚠")










#Problem 04: BUSINESS MANAGEMENT

#4.1 Array creation
#Function that'll load the .csv file into numpy array
def create_numpy_array(data):
    """
    Converts data of .csv file into numpy array

    Parameters:
    salaries(str): path of .csv file

    Return:
    arr(numpy.ndim): numpy array 
    """
    return np.loadtxt(data, delimiter=",")


#Specifying the path of salaries.csv
path = "../Data_set/salaries.csv"
data = create_numpy_array(path)

#Print numpy array
print(f"Equivalent numpy array of .csv file is: \n {data[:15]}")




#4.2 Mothwise
#Function that'll create mothwise(2D) array
def create_monthwise_data(data):
    """
    Create a monthwise 2D array

    Parameters:
    salaries(numpy.ndim): numpy array

    Returns:
    arr(numpy.ndim): 
    """

    #Compute multiple of 12 
    num_rows = data.shape[0] // 12 * 12
    #Return a month-wise 2D numpy array
    return data[:num_rows].reshape(12, -1, data.shape[1])

#Compute monthwise data
monthwise_data = create_monthwise_data(data)
#Print month wise data
print(f"Moth wise data is: ")
monthwise_data




#4.3 A Specific Month
#Function that'll compute monthwise data
def specific_month(monthwise_data, month_num):
    """
    Function that'll return the data of specified month

    Parameters:
    month_wise(numpy.ndim): Input numpy array

    Return:
    specific_month_data(numpy.ndim): Data of specified month
    """
    if 0 <= month_num <= 12:
        return monthwise_data[month_num - 1]
    else:
        return "Invalid month number"

#Function used to receive and return month number and data of specified month
def specific_month_details():
    """
    Function that'll receive and return month number and data of specified month

    Parameters:
    None

    Return:
    month_num(int), specific_month_data(numpy.ndim): Month number and data of specified month
    """
    month_num = int(input("👉Enter a valid month number (valid range: [1, 12]): "))
    return month_num, specific_month(monthwise_data, month_num)

#Get month number and data of specified month
data_getter = specific_month_details()
print(f"➤Data of specified month '{data_getter[0]}' is: ")
data_getter[1]





#4.4 Adding new rows
#Function that's used to  add new rows to the specified month
def adding_new_rows(monthwise_data, new_data_row):
    """
    Function that'll add new rows

    Parameters:
    monthwise_data(numpy.ndim), new_data_row(tuple): Input numpy array of specified month and shape
    of specified month

    Return:
    new_specific_month_data(numpy.ndim): New month data
    """
    #Compute current number of days within a specified month
    max_days = specific_month_data.shape[0]
    
    #Validating the range of days (By assuming each month have 30 days)
    if max_days <= 30:
        return np.vstack((specific_month_data, np.ceil(np.random.rand(new_data_row[1])*500)))
    else:
        return "Moth range exceeded by 30"
        

#Get data of specified month
specific_month_data = specific_month_details()[1]
#Add new data to the specified month
print("\nAfter adding data of one more month: ")
adding_new_rows(specific_month_data, specific_month_data.shape)





#4.5 Adding new people
#Function that's used to add new peoples
def add_new_employees(specific_month_data):
    """
    This function will add new employees to data
    
    Parameters:
    num_emp(int), specific_month_data(numpy.ndim): Number of employees to add and add
    to specific month

    Return:
    (numpy.ndim): New numpy array
    """
    return np.hstack((specific_month_data, np.zeros((specific_month_data.shape[0], 1))))

add_new_employees(specific_month_data)




#4.6 Statistics
#Simple desing function
def design():
    print("=+=" * 40, end="")
    

#Function used to compute statistics
def statistics(data):
    """
    This function'll calculate the statistics like, mean, sd, etc

    Parameters:
    data(numpy.ndim): Input numpy array

    Return:
    None
    """
    design();print(f"\t🫵 Total income of employees is: {np.sum(data)}\n"); design()
    print(f"\t🫵 Mean of per-person is: {np.mean(data, axis=0)}\n"); design()
    print(f"\t🫵 Standard devation of per-person is: {np.std(data, axis=0)}\n"); design()
    print(f"\t🫵 Mean of day wise is: {np.mean(data, axis=1)}\n"); design()
    print(f"\t🫵 Standard devation of day wise is: {np.std(data, axis=1)}\n"); design()

statistics(data)




