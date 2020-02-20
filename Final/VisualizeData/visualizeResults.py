import matplotlib.pyplot as plt
import pandas as pd

def readResult(fileName):
    results = []
    with open(fileName, 'r') as f:
        line = f.readline()
        while line!='':
            result = line.rstrip().split()
            for i in range(len(result)):
                if i == 0:
                    result[i] = int(result[i])
                else:
                    result[i] = float(result[i])
            results.append(result)
            line = f.readline()
    print(results)
    return results

import numpy as np
def visualizeResult(results):
    data = results
      
    matrix_size = []
    runtime_python = []
    runtime_c = []
    runtime_numpy = []
    
    for i in range(len(data)):
        matrix_size.append(data[i][0])
    for i in range(len(data)):
        runtime_python.append(data[i][1])
        runtime_c.append(data[i][2])
        runtime_numpy.append(data[i][3])
    
    X = np.arange(len(data))
    plt.bar(X + 0.00, runtime_python, color = 'b', width = 0.25)
    plt.bar(X + 0.25, runtime_c, color = 'g', width = 0.25)
    plt.bar(X + 0.50, runtime_numpy, color = 'r', width = 0.25)
    
    
    plt.xlabel('Matrix Size')
    plt.ylabel('RunTime (Seconds)')
     
    plt.show()

if __name__=='__main__':
    results = readResult('result.txt')
    visualizeResult(results)