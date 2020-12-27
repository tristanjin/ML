import pandas as pd

array1 = pd.Series([1,2,3],index=['a','b','c'])
array2 = pd.Series([4,5,6],index=['b','c','d'])

array = array1.add(array2,fill_value=0)
print(array)
array3 = array1.add(array2)
print(array3)

arr1 = pd.DataFrame([[1,2],[3,4]],index=['a','b'])
arr2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['b','c','d'])
print(arr1)
print(arr2)

arr = arr1.add(arr2,fill_value=0)
print(arr)
print('sum of column1:', arr[1].sum())
print(arr.sum())