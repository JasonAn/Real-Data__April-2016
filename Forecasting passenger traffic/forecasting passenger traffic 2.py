import numpy as np
import sys

N = int(input())
Data = np.zeros(12)

for i in range(N / 12 * 12):
    userinput = sys.stdin.readline()
    words = userinput.split()
    Data[i % 12] += int(words[1])


for i in range(12):
    Data[i] = Data[i] / ( N / 12)
    print int(y_p[i])

#plt.plot(x, Data)
# y = np.hstack([Data[0:60],y_p])
# y = np.hstack([y, Data[60:]])
# plt.plot(y)
# plt.show()
# z_p = rbf(x_p)
#print y_p



