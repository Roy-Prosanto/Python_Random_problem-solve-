import  numpy as np

# Problem 01
generate =np.arange(5)
print(generate)
print(np.random.normal(size =6),"\n")

# Problem 17
np.random.seed(32)
nums=  np.random.randint(low=0,high=256,size=(300,400,5))
print(nums,"\n")

# problem 3 3x3x3
n= np.random.random((3,3,3))
print(n,"\n")

# Problem  4 ( 5x5 )
random = np.random.random((5,5))
print(random)
print(np.max(random))
print(np.min(random))

# Problem  05 (10x4)
n=np.random.random((10,4))
print(n)
print( " 5 Row ")
y=n[:5,:]
print(y,"\n")

# Problem 06 (shuffle and  permutation ) 
r= np.arange(10)
print(r)
print("Shuffle")
np.random.shuffle(r)
print(r)
print("permutation")
print(np.random.permutation(r),"\n")

# problem 07 3x3 matrix
print("3x3 matrix")
matrix= np.random.random((3,3))
print(matrix)
print("  normal matrix ")
print(np.random . normal(matrix))
print("  normalize ")
matrix_max,matrix_min= matrix.max(),matrix.min()
matrixs=(matrix-matrix_min)/(matrix_max-matrix_min)
print(matrixs)
print("\n")

# problem 08
random = np.random.random(10)
print(random)
print("Sort value :")
print(np.sort(random))
print("\n")

# Problem 09
nump =np.random.uniform(1,12,5)
v=4
n = nump.flat[np.abs(nump - v).argmin()]
print(n)
print("\n")

# problem  10 
frist_random  =  np.random.randint(0,2,6)
secend_random = np.random.randint(0,2,6)
result_random = np.equal(frist_random,secend_random)
print(result_random)
print(" Other random equal ")
print(np.allclose(frist_random,secend_random))
print("\n")
# problem 11
randoms= np.random.random(15)
randoms[randoms.argmax()]=1
print(randoms)
print("\n")


# problem 12
pro =  np.random.random((10,2))
x,y = np.atleast_2d(pro[:,0], pro[:,1])
d = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
print(d)
# Problem  13
ns= np.random.randint(0,10,10)
print(ns)
nsp= np.bincount (ns).argmax()
print(ns,"\n")

# problem 14
ps= np.random.random((10,2))
x,y= ps[:,0],ps[:,1]
r =(x**2+y**2)
t= np.arctan2(y,x)
print(t,"\n")


# problem 15 closer
ns= np.random.randint(0,100)
print(ns)
print(" next closer ")
nsp= np.abs(ns)
print(nsp,"\n")