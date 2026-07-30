import numpy as np

a = np.arange(1,6)
b= np.arange(10,60,10)


multi = np.multiply(a, b)
divi = np.divide(a,b)
sub = np.subtract(a,b)
square = np.square(a)
add = np.add(a,b)

print(add)





partb = np.arange(1,21)

evn = partb[partb%2 == 0 ]
biggerThenTen = partb[partb > 10]

print(evn, biggerThenTen)


#3x3

ndm = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(ndm.T)
print(np.transpose(ndm))

print(ndm.sum(1))