from numpy import asarray
import numpy as np
from numpy.linalg import norm
from PIL import Image
def extractVect (M) : #extracts the first vector column of the first matrix of the tensor
 new_list = []
 for i in range(len(M[0])) :
     new_list.append(M[0][i][0])
 new_vect = np.array(new_list)
 return(new_vect)
image = Image.open('cat.jpg')
#converting the image into a 3d tensor and displaying a chosen matrix from it
data = asarray(image)
print("here's an extracted matrix from the tensor : ")
print(data[0])
#extacting a random column vector from this tensor and displaying it
print("here's an extracted 1st column vector from the previous matrix : ")
print(extractVect(data))
print("The L1 norm of this vector is : ")
print(norm(extractVect(data),1))
print("The L2 norm of this vector is : ")
print(norm(extractVect(data)))