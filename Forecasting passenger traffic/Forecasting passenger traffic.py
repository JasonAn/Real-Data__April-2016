import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
import sys

N = int(input())
Data = np.zeros(2*N)


x1 = np.linspace(1, N, N)
x2 = np.linspace(N + 13, 2 * N + 12, N)
x = np.hstack([x1, x2])

x_p = np.linspace(N + 1, N + 12, 12)


for i in range(N):
    userinput = sys.stdin.readline()
    words = userinput.split()
    print i, N + i
    Data[i] = int(words[1])
    Data[N + i] = Data[i]

ius = InterpolatedUnivariateSpline(x, Data)
# print x
# print x_p
rbf = Rbf(x, Data)
y_p = rbf(x_p)
for i in range(12):
    print int(y_p[i])
#plt.plot(x, Data)
# y = np.hstack([Data[0:60],y_p])
# y = np.hstack([y, Data[60:]])
# plt.plot(y)
# plt.show()
# z_p = rbf(x_p)
#print y_p



