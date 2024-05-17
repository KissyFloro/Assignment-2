# flatten method is used to flatten a multi-dimensional array into a one-dimensional array


# Example 1:
import numpy as np
x = np.array([[12,29], [45,96]])
result = x.flatten()
print(result)

# Example 2:
import numpy as np
x = np.array([[1,12,3], [5,11,13]])
result = x.flatten()
print(result)

# Example 3:
import numpy as np
x = np.array([[[1,3,7],[9,8,5]], [[6,7,7], [5,13,4]]])
result = x.flatten()
print(result)
