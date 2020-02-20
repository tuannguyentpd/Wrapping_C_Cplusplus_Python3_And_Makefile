import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from mpl_toolkits.mplot3d import Axes3D


def getMNISTData():
    digits = datasets.load_digits()
    
    X = digits.data[:]
    y = digits.target[:]
    
    labels = digits.target_names
    
    return X, y, labels

def getIRISData():
    iris = datasets.load_iris()
    
    X = iris.data[:]
    y = iris.target[:]
    
    labels = iris.target_names
    
    return X, y, labels

def getWINEData():
    wine = datasets.load_wine()
    
    X = wine.data[:]
    y = wine.target[:]
    
    labels = wine.target_names
    
    return X, y, labels

def getBREASTCANCERData():
    breast_cancer = datasets.load_breast_cancer()
    
    X = breast_cancer.data[:]
    y = breast_cancer.target[:]
    
    labels = breast_cancer.target_names
    
    return X, y, labels

def readData():
    pass

def dimensionReduce_TSNE(data, components):
    tnse = TSNE(n_components = components, random_state = 0)
    return tnse.fit_transform(data)

def dimensionReduce_PCA(data, components):
    pca = PCA(n_components = components, random_state = 0)
    return pca.fit_transform(data)

import matplotlib as mpl
def getColor(c, N, idx):
    cmap = mpl.cm.get_cmap(c)
    norm = mpl.colors.Normalize(vmin=0.0, vmax=N - 1)
    return cmap(norm(idx))

def visualizeData_3D(X_3d, y, labels, grid):
    target_ids = range(len(labels))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w', 'orange', 'purple'
    for i, c, label in zip(target_ids, colors, labels):
        ax.scatter3D(X_3d[y == i, 0], X_3d[y == i, 1], X_3d[y == i, 2], c=c, label=label)
    
    if grid == False:
        plt.axis('off')
        #plt.grid(b=None)
    
    plt.legend()
    plt.show()

def visualizeData_2D(X_2d, y, labels, grid):   
    target_ids = range(len(labels))
    
    fig = plt.figure()
    colors = 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w', 'orange', 'purple'
    for i, c, label in zip(target_ids, colors, labels):
        plt.scatter(X_2d[y == i, 0], X_2d[y == i, 1], c=c, label=label)
        
    if grid == False:
        plt.axis('off')
        #plt.grid(b=None)
    
    plt.legend()
    plt.show()
    


''' ---------- main --------- '''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--grid', action='store_false', help='Hien thi luoi cho bieu do')
parser.add_argument('--d', type=int, help='Dimensions - So chieu du lieu visualize', default=3)
parser.add_argument('--alg', type=str, default='tsne', help='Algorithm - Thuat toan gian chieu du lieu - TSNE/PCA')
opt = parser.parse_args()

'''
# Cau truc du lieu:
# X[i]: (vector) - data cua diem du lieu thu i
# y[i]: (list<string/numeric/...>) - label cua diem du lieu thu i
# labels: (list<string/numeric/...>) - tat ca cac labels cua bo du lieu
'''
X, y, labels = getMNISTData()

if opt.d == 2:
    if opt.alg.lower() == 'pca':
        X_2d = dimensionReduce_PCA(X, 2)
    else:
        X_2d = dimensionReduce_TSNE(X, 2)
    visualizeData_2D(X_2d, y, labels, opt.grid)
else:
    if opt.alg.lower() == 'pca':
        X_3d = dimensionReduce_PCA(X, 3)
    else:
        X_3d = dimensionReduce_TSNE(X, 3)
    visualizeData_3D(X_3d, y, labels, opt.grid)