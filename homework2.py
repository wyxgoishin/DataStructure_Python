import math
import numpy as np

def cal_k(x1, x2, y, h):
    # matrix_k = [[1 + 50 * h / 4, (3 + 2 * math.sqrt(3)) / 12 * 50 * h], 
    #             [(3 - 2 * math.sqrt(3)) / 12 * 50 * h, 1 + 50 * h / 4]]
    # matrix_right = [[-50 * y + 49 / 50 * math.exp(-x1) + x1 + 1 / 50],
    #                 [-50 * y + 49 / 50 * math.exp(-x2) + x2 + 1 / 50]]
    matrix_k = [[1 + 300 * h / 4, (3 + 2 * math.sqrt(3)) / 12 * 300 * h], 
                [(3 - 2 * math.sqrt(3)) / 12 * 300 * h, 1 + 300 * h / 4]]
    matrix_right = [[-300 * y + 599 * math.exp(-x1 / 5) - 300],
                    [-300 * y + 599 * math.exp(-x2 / 5) - 300]]
    return  np.linalg.inv(np.array(matrix_k)) @ np.array(matrix_right)

def get_k(x, y, h):
    x1, x2 = x + (3 + math.sqrt(3)) / 6 * h, x + (3 - math.sqrt(3)) / 6 * h
    return np.ravel(cal_k(x1, x2, y, h)).tolist()


def savepoint(x, a, h):
    compare_list = [0, a, a + (3 - a) / 4, a + (3-a) / 2, a + 3 * (3 - a) / 4, 3]

    def equal(x, y, h):
        return abs(x - y) < h * 0.5

    for i in compare_list:
        if equal(x, i, h):
            return True
    return False

def real_y(x):
    # return math.exp(-50 * x) + (math.exp(-x) + x) / 50
    return math.exp(-300 * x) + 2 * math.exp(-x / 5)


# h1, h2, x0, y0 = 1e-2, 1e-1, 0, 51 / 50 
# a, x, y = 0.4605, x0, y0
h1, h2, x0, y0 = 1e-3, 1e-1, 0, 3
a, x, y = 0.07575, x0, y0
result = [[], [], []]
while x <= 3:
    h = h1 if x <= a else h2
    if savepoint(x, a, h):
        result[0].append(y)
    k1, k2 = get_k(x, y, h)
    y = y + h / 2 * (k1 + k2)
    x = x + h

# del result[0][2]

x, y = x0, y0
while x<=3:
    h = h1
    if savepoint(x, a, h):
        result[1].append(y)
    k1, k2 = get_k(x, y, h)
    y = y + h / 2 * (k1 + k2)
    x = x + h

cal_list = [0, a, a + (3 - a) / 4, a + (3-a) / 2, a + 3 * (3 - a) / 4, 3]
for i in cal_list:
    result[2].append(real_y(i))

err = []
err.append(abs(1 - np.array(result[0]) / np.array(result[2])))
err.append(abs(1 - np.array(result[1]) / np.array(result[2])))
err = np.array(err)


print('比较点值：         ' + str(cal_list))
print('步（2）的结果：    ' + str(result[0]))
print('步（3）的结果：    ' + str(result[1]))
print('精确解：           ' + str(result[2]))
for j in range(2):
    method = '步（%d)' % (j + 2)
    for i in range(len(err[j])):
        if i == 0:
            print(method + '的计算误差为:[%.4e,' % err[0][i], end='')
        elif i == len(err[j]) - 1:
            print('%.4e]' % err[j][i])
        else:
            print('%.4e,' % err[j][i], end='')