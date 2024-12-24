xau= input()
CH=0
CT=0
CS=0
for i in xau:
    if i.isupper():
        CH+=1
    elif i.islower():
        CT+=1
    elif i.isdigit():
        CS+=1
print("so chu hoa:{0}, so chu thuong:{1}, so chu so:{2}".format(CH,CT,CS))