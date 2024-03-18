#Text files ar,rt,wt,xt
#binary files ab,rb,wb,xb

#file handler = open(filename, mode)

'''
f=open("msg.txt","rt")
print(f.read())
f.close()



nm=" Rahul Went to play football"
f=open("msg.txt","a")
f.write(nm)
f.close()


f=open("msg.txt","rt")
print(f.read())
f.close()
'''

nm1="DYPIMR"
f=open("newfile.txt","wt")
f.write(nm1)
f.close()

f=open("newfile.txt","rt")
print(f.read())
f.close()




