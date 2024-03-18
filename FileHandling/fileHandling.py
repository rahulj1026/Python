'''
nm1="DYPIMR"
f=open("newfile.txt","wt")
f.write(nm1)
f.close()

f=open("newfile.txt","rt")
print(f.read())
f.close()
'''

'''
nm2="Rahul Jadhav"

f=open("second.txt","xt")
f.write(nm2)
f.close()
'''





'''
nm2=" Pursuing MCA"

f=open("second.txt","a")
f.write(nm2)
f.close()

f=open("second.txt","r")
print(f.read())
f.close()
'''

f=open("Demo.txt","rt")

f.seek(4)

#print(f.read())

#print(f.readline(5)) #u can specify how many charecters you want to print

print(f.readlines(10))
f.close()
