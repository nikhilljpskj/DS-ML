import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
result_add = arr1 + arr2
result_multiply = arr1 * arr2
mean_result_add = np.mean(result_add)
max_result_multiply = np.max(result_multiply)
print("Addition:",result_add)
print("Multi:",result_multiply)
print("Mean Add:",mean_result_add)
print("Max Mul:",max_result_multiply)
