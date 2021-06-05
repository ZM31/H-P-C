def max_value(c,a):
    f = open(c)
    txt = f.readlines()
    txt1 = []
    b = len(txt)
    b = int(int(b) / 3)
    i = int(a) * b
    j = (int(a) + 1) * b
    if a == 2:
        j = b  # find start and end index:i,j

    for m in range(i,j):
        txt1.append(eval(txt[m].strip('\n')))
    txt1.sort(reverse=True)

    f.close()
    return  txt1     #return max value
def maxzhishu(list,data):
    for i in range(len(list)):
        if data%list[i]!=0:
            return  list[i]     #return max value
    else:
        return 0    # return 0 : if  no number can huzhi



if __name__=='__main__':
    print(max_value('setup3.txt','0'))