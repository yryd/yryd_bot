import random

"""xdx例如4d6为掷4个骰子的和"""
def random_n1dn2(num_1, num_2):
    sum = 0
    for i in range(int(num_1)):
        i = random.randint(1, int(num_2))
        sum = sum + i
    return sum

#固定六面骰num_1个，取num_2次最大
def random_maxn_nd6(n_1, n_2):
    sum_list = []
    for i in range(int(n_2)):
        i = random_n1dn2(n_1, 6)
        sum_list.append(i)
    sum_list.sort(reverse=True)
    return sum_list[0]

if __name__ == '__main__':
    print(random_n1dn2(2,6))
    print(random_maxn_nd6(3, 4))
