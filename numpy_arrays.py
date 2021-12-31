import numpy as np
print("NumPy version is ", np.__version__)

## 1-D array..........................
array_1 = np.array([1,2,3,4,5])

print("array_1 \n", array_1)

## 2-D array..........................
array_2 = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)

print("array_2 \n", array_2)

# 3-D array...........................
array_3 = np.array(
    [
        [
            [1,2,3],
            [4,5,6]
        ],
        [
            [7,8,9],
            [10,11,12]
        ]
    ]
)

print("array_3 \n", array_3)

print("Number of dimensions:")
print(array_1.ndim)
print(array_2.ndim)
print(array_3.ndim)