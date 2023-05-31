import numpy as np
nums_f = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
nums_s = [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
nums_t = [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]

matrix = [nums_f, nums_s, nums_t]
result = np.corrcoef(matrix)
print(result)