import numpy as np

# TWORZENIE NOWYCH TABLIC NA PODSTAWIE LIST

# arr = np.array([1, 2, 3 ,4, 5])
# print(arr)
# print(type(arr))

# arr_2d = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
# ])
# print(arr_2d)

# TYPY DANYCH

# arr_int = np.array([1,2,3,4,5], dtype='i')
# print(arr_int)
# print(arr_int.dtype)

# TWORZENIE TABLIC PRZY UZYCIU FUNKCJI NUMPY

# print(np.zeros(10, dtype='i'))
# print(np.zeros((5, 5)))

# print(np.ones((3, 3)))

# print(np.linspace(0, 10, 6))

# print(np.eye(5))

# print(np.random.rand(5))
# print(np.random.rand(3,2))

# print(np.random.randn(5,5))

# print(np.random.randint(1,49,(3,6)))

# INDEKSOWANIE DANYCH W TABLICACH

# arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
# print(arr_2d)
# print(arr_2d[0])
# print(arr_2d[1,2])
# print(arr_2d[:,1])
# print(arr_2d[-1,-1])

# matrix = np.random.randint(1,100, (5,5))
# print(matrix)
# print(matrix[1:4, 1:4])

# KSZTALT TABLICY I JEGO MODYFIKACJA

# arr = np.ones((5,4))
# print(arr)
# print(arr.shape) #sprawdza ksztalt tablicy

# arr = np.ones(25)
# print(arr)
# print(arr.reshape((5,5)))

# arr = np.random.randint(1,100,10)
# print(arr)
# print(arr.min())
# print(arr.max())
# print(f'wartosc najwieksza:  {arr.max()}, pozycja wartosci najwiekszej:  {arr.argmax()}')
# print(f'wartosc najmniejsza:  {arr.min()}, pozycja wartosci najmniejszej:  {arr.argmin()}')

# FUNKCJE MATEMATYCZNE W NUMPY

# arr = np.arange(11)
# print(arr)
# print(np.sqrt(arr))
# print(np.exp(arr))

# ARYTMETYKA I ALGEBRA TABLIC

arr0 = np.random.randint(1,10, (3,3))
arr1 = np.random.randint(1,10, (3,3))
print(arr0,arr1)
print(arr0 + arr1)
print(arr0 - arr1)
print(arr0 * arr1)
print(arr0 ** 2)

print(arr0.dot(arr1)) #iloczyn skalarny
print(arr0[0].dot(arr1[1]))


# ZADANIA

# 1
