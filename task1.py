def max_value(c,a):
    f = open(c)
    txt = f.readlines()

    b = len(txt)
    b = int(int(b) / 3)
    i = int(a) * b
    j = (int(a) + 1) * b
    if a == 2:
        j = b  # find start and end index:i,j


    max = eval(txt[i].strip('\n'))
    for k in range(i, j):
        if eval(txt[k].strip('\n')) > max:
            max = eval(txt[k])  # find max value

    f.close()
    return  max     #return max value


if __name__=='__main__':
    print(max_value('setup1.txt','2'))