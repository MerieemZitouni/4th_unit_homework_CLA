from PIL import Image
from numpy import asarray
import numpy as np
def isSquare (M):
     return all (len (row) == len (M) for row in M)
image = Image.open('cat.jpg')
#converting the image into a 3d tensor
data = asarray(image)
#extracting a random matrix from the tensor and displaying it
mtrx = np.array(data[7])
print(mtrx)
#verifying that this matrix is not a square matrix
# so the matrix is not a diagonale, nor a triangular or identity matrix
print(isSquare(mtrx)) 
print("this matrix is not a diagonale, nor a triangular or identity matrix")
