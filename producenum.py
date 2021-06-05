import random
def summ(filepath ,num):
    fp = open(filepath,'w')
    for i in range(num):
        a = random.randint(100,7000000)
        if i != num-1 :
            fp.write(str(a)+'\n')
        else:fp.write(str(a))
    fp.close()



if __name__=='__main__':
    (summ('setup3.txt',100000))