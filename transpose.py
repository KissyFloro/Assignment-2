#Transpose method is used to transpose an array


#Example 1:
import numpy as np
x = np.array([[4,2], [3,8]])
result = x.transpose()
print(result)

#Example 2:
import numpy as np
x = np.array([[1,2,3], [4,5,6]])
result = np.transpose(x)
print(result)

#Example 3:
import numpy as np
x = np.array([[[1,3], [1,2]], [[0,5], [6,9]]])
result = np.transpose(x, (1,0,2))
print(result)