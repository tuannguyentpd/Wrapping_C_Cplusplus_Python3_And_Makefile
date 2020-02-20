import time
from ctypes import cdll
import ctypes
from ctypes import *

''' Dung thu vien dong C '''
# matrix_lib.mtrix_Multi.argtypes = [POINTER(POINTER(c_int)), c_int, c_int, POINTER(POINTER(c_int)), c_int, c_int]

matrix_lib = cdll.LoadLibrary("multi_matrix.so")
multi_matrix = matrix_lib.matrix_Multi
multi_matrix.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.c_int, ctypes.c_int]
print_matrix = matrix_lib.print_Matrix
print_matrix.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.c_int, ctypes.c_int]
random_matrix = matrix_lib.random_Matrix
random_matrix.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.c_int, ctypes.c_int]
sort_array = matrix_lib.sortArray
sort_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
print_array = matrix_lib.printArray
print_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
random_array = matrix_lib.randomArray
random_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]


sum_int = matrix_lib.sum
minus_int = matrix_lib.minus
mul_int = matrix_lib.mul
div_int = matrix_lib.div_
mod_int = matrix_lib.mod

def print_sum(a, b):
    print("%d + %d = %d"%(a, b, sum_int(a, b)))
          
def print_minus(a, b):
    print("%d - %d = %d"%(a, b, minus_int(a, b)))
              
def print_mul(a, b):
    print("%d * %d = %d"%(a, b, mul_int(a, b)))
              
def print_div(a, b):
    print("%d / %d = %d"%(a, b, div_int(a, b)))
              
def print_mod(a, b):
    print("%d mod %d = %d"%(a, b, mod_int(a, b))) 

def mulMatrix(a, na, ma, b, nb, mb):
    random_matrix(a, na, ma)
    print_matrix(a, na, ma)
    random_matrix(b, nb, mb)
    print_matrix(b, nb, mb)
    
    print_matrix(multi_matrix(a, na, ma, b, nb, mb), na, mb)
    
def print_cal_CLib(a, b):
    print_sum(a, b)
    print_minus(a, b)
    print_mul(a, b)
    print_div(a, b)
    print_mod(a, b)
    
    
''' Dung code python '''

def print_sum_py(a, b):
    print("%d + %d = %d"%(a, b, a+b))
          
def print_minus_py(a, b):
    print("%d - %d = %d"%(a, b, a-b))
              
def print_mul_py(a, b):
    print("%d * %d = %d"%(a, b, a*b))
              
def print_div_py(a, b):
    print("%d / %d = %d"%(a, b, a/b))
              
def print_mod_py(a, b):
    print("%d mod %d = %d"%(a, b, a%b)) 
    
def print_cal_pyDev(a, b):
    print_sum_py(a, b)
    print_minus_py(a, b)
    print_mul_py(a, b)
    print_div_py(a, b)
    print_mod_py(a, b)   
  

def main():
    na = ma = 3
    nb = 3
    mb = 2
    #a = array('l', [[3,5,34],[45,56,46],[45,23,3]])
    #b = array('l', [[346,46],[56,67],[4,4]])
    a = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))()
    b = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))()

    
    
    random_matrix(a, na, ma)
    print_matrix(a, na, ma)
    random_matrix(b, nb, mb)
    print_matrix(b, nb, mb)
    print('Inited!')
    
    print_matrix(multi_matrix(a, na, ma, b, nb, mb), na, mb)
    
def sort_arr_CLib(a, n):
    sort_array(a, n)

def sort_arr_pyDev(a, n):
    if n<2: return
    for i in range(n-1):
        for j in range(1, n):
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    

    
import numpy as np
import random  
if __name__=='__main__':
    #Sort Array - python code
    n_pyDev = 10000
    arr_pyDev = np.random.randint(10000, size=n_pyDev)
    start_time = time.time()
    sort_arr_pyDev(arr_pyDev, n_pyDev)
    finish_time = time.time()
    runtime_py = finish_time - start_time
    print("Python_InterchangeSort: Program excuted in %s seconds ---" % (runtime_py))    

    #Sort Array python wrapped C
    n_CLib = ctypes.c_int(10000)
    arr_CLib = (ctypes.c_int * n_CLib.value)()
    random_array(arr_CLib, n_CLib)
    cast(arr_CLib, ctypes.POINTER(ctypes.c_int))
    start_time = time.time()
    sort_arr_CLib(arr_CLib, n_CLib)
    finish_time = time.time()
    runtime_c = finish_time - start_time
    print("C_InterchangeSort: Program excuted in %s seconds ---" % (runtime_c))
    
    print("Ctypes nhanh hon Python: %.5f lan"%(runtime_py/runtime_c))
    
    
    ''' 
    a = 346
    b = 3667
    
    start_time = time.time()
    print_cal_CLib(a, b)
    finish_time = time.time()
    print("C: Program excuted in %s seconds ---" % (finish_time - start_time))
    
    start_time = time.time()
    print_cal_pyDev(a, b)
    finish_time = time.time()
    print("Python: Program excuted in %s seconds ---" % (finish_time - start_time))
    '''