from PIL import Image
from numpy import asarray
import numpy as np
def isSquare (M):
     return all (len (row) == len (M) for row in M)
def isUpperTriangle (M) :
     if isSquare(M) == False :
          return(False)
     k = M.shape[0]
     for i in range(k):
          for j in range(i):
               if M[i,j] != 0 :
                    return(False)
     else : 
          return(True)
def isLowerTriangle (M) :
     if isSquare(M) == False :
          return(False)
     k = M.shape[0]
     for i in range(k):
          for j in range(i):
               if M[j,i] != 0 :
                    return(False)
     else : 
          return(True)

def isDiagonal (M):
     if (isUpperTriangle(M)) and (isLowerTriangle(M)) :
          return(True)
     else :
          return(False)

image = Image.open('cat.jpg')
#converting the image into a 3d tensor
data = asarray(image)
#extracting a random matrix from the tensor and displaying it
mtrx = np.array(data[7])
print(mtrx)
#verifying the type of the matrix
print("This matrix is : ")
if (isUpperTriangle(mtrx)) :
     print("upper triangular")
else :
     print("is not upper triangular")
if (isLowerTriangle(mtrx)) :
     print("Lower triangular")
else :
     print("is not Lower triangular")
if (isDiagonal(mtrx)) :
     print("Diagonal")
else :
     print("not diagonal")     
