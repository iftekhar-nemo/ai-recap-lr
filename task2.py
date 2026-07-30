import numpy as np

a = np.arange(1,6)
b= np.arange(10,60,10)


multi = np.multiply(a, b)
divi = np.divide(a,b)
sub = np.subtract(a,b)
square = np.square(a)
add = np.add(a,b)

print("Summation :", add, "Substraction:", sub, "Divition :", divi, "Square : ", square, "Multiply: ", multi)





partb = np.arange(1,21)

evn = partb[partb%2 == 0 ]
biggerThenTen = partb[partb > 10]

print("Even Number :", evn, "Number is bigger than 10: ", biggerThenTen)

ndm = np.array([[10,20,30], [40,50,60], [70,80,90]])
print("Matrix transpose only usin T :", ndm.T)
print("Matrix transpse using np  transpose method: ", np.transpose(ndm))

print("Raw summation: ", ndm.sum(1))
print("Column summation: ", ndm.sum(0))