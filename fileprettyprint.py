f=open('code.txt','r')
f1=open('newcode.txt','w')
for i in f:
    i=i.strip('\n')
    i=i.rstrip()
    if i.endswith(';'):
        i=i[:-1]
    count_spaces=0
    count_tabs=0
    #print (i)
    for j in i:
        if j==' ': count_spaces+=1
        else: break
    half_space=count_spaces//2
    #print (half_space)
    i=(' '*half_space)+(i.lstrip())
    print (i)
    f1.write(i)
    f1.write('\n')
f.close()
f1.close()
