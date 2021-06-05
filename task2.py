def summ(a,num):
    sum=0
    b = int(int(num) / 3)
    i = int(a) * b
    j = (int(a) + 1) * b
    if a == 2:
        j = b+1  # find start and end index: i,j
    if a == 0:
        i = 2
    for k in range(i, j):
        for i in range(2,k):
            if k % i == 0:
                break
        else:sum+=1   # sum for zhihshu


    return  sum   # return sum value


if __name__=='__main__':
    print(summ('setup2.txt','0'))