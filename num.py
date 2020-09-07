""" Numpy Basics ----> Dilpreet Singh Kohli """

import numpy as np                                    #Importing Numpy


#Single Dimension Array
a = np.array([1,2,3])
print (a)

print()

#Multi Dimension Array
b = np.array([(1,2,3),(5,6,7)])
print (b)

print(b[0])                                           #OUTPUT --> [1,2,3]
print(b[1])                                           #OUTPUT --> [5,6,7]
print(b[1][1])                                        #OUTPUT --> 6

print()
print()

#Numpy Operations

# ndim ---> is used to find number of dimensions in an array

a = np.array([1,2,3])                                #OUTPUT --> 1
print (a.ndim)

b = np.array([(1,2,3),(4,5,6)])                      #OUTPUT --> 2
print (b.ndim)

print ()

# itemsize  ---> we can calculate the byte size of each element in array

print (a.itemsize)                                  #OUTPUT ---> 4  it elemeny occupies 4byte


# dtype ---> you can find the data type of an array

print (a.dtype)                                     #OUTPUT  ---> INT32

a = np.array([1,2,3,4,5], dtype='i8')
print (a.dtype)                                     #OUTPUT  ---> INT64

print()
print()

# Size and shape

a = np.array([(1,2,3,4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print (a.size)                                      #Size will give you the output of total elements in an array
print (a.shape)                                     #Shape will give you (rows,columns)  ---> (1,6) 
print (b.shape)                                     #OUTPUT ---> (2,3) 2 rows adn 3 columns


print()
print()

# Reshape the number of rows and columns

a = np.array([(1,2,3,4),(5,6,7,8)])
print (a)
print (a.shape)                                

print ()

""" 
                                 1 2 3 4  --> Number of columns

so basically it is like this     1 2 3 4    row_1
                                 5 6 7 8    row_2

so we will reshape it to this:
                                 1 2  --> Number of columns

                                 1 2        row_1
                                 3 4        row_2
                                 5 6        row_3
                                 7 8        row_4
                                 
"""
a = a.reshape(4,2)
print(a)
print(a.shape)


print()
print()


# Slicing
print (a)

print (a[0])        #OUTPUT ---> [1,2]
print (a[3])        #OUTPUT ---> [7,8]
print (a[3,0])     #OUTPUT ---> 7


print()

# MIN/MAX
a = np.array([1,2,5])

print (a.min())
print (a.max())
print (a.sum())

#linspace

z = np.linspace(2,10)             #(start,stop,step)
print (z)

print()

z = np.linspace(2,10,5)           #(start,stop,step)
print (z)

z = np.linspace(2,10,9)           #(start,stop,step)
print (z)

print()

a = np.zeros(5)
print (a)
print (type(a[0]))

print ()

b = np.ones(5)
print (b)


print()


# Note: IN Numpy Arrays rows are called axis 1 and columns are called axis 0
#to calculate the columns

a = np.array([(1,2,3),(3,4,5)])
print (a)
print (a.sum(axis=0))                       # 1+3=4, 2+4=6 and 3+5=8


print()

b = np.array([(1,2,3),(4,5,6)])
print(b)
print (a.sum(axis=1))                        # 1+2+3 = 6, 4+5+6 = 12

print()
print()


#There are Various mathematical operations you can perform

#SquareRoot
a = np.array([(4),(2)])
print (np.sqrt(a))

a = np.array([(2,4,9),(10,15,20)])
print (np.sqrt(a))

print ()


x = np.array([(6,5,8),(9,5,7)])
y = np.array([(1,2,3),(1,2,3)])
print (x+y)                                  #Addition
print()
print (x-y)                                  #Subtraction
print ()
print (x*y)                                  #Multiplication
print ()
print (x/y)                                  #Division


print()
print()


# Vertical & Horizontal Stacking

x= np.array([(1,2,3),(4,5,6)])
y= np.array([(7,8,9),(10,11,12)])
print(np.vstack((x,y)))

print()

print(np.hstack((x,y)))


print()
print()

# ravel   ---> use to convert one numpy array into a single column

a = np.array([(1,2,3),(4,5,6)])
print (a)

print ()

print (np.ravel(a))