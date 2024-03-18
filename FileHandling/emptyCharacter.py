'''
#Blank Character
f=open("open.txt","r")
cnt=0
for x in f.read():
    if(x==' '):
        cnt=cnt+1
print(cnt)


#new line
f=open("open.txt","r")
cnt=0
for x in f.read():
    if(x=='\n'):
        cnt=cnt+1
print(cnt)

f.close()
'''

"""
#Example 3
f=open("open.txt","r+")
print("Old Content of the file")
print(f.read())

str="*****"

f.seek(6)
f.write(str)

f.seek(0)
print("New content")
print(f.read())
f.close()
"""

#WRITELINES
subject=["Python\n", "OT\n","SPM\n","ADBMS"]
f=open("open.txt","w")
f.writelines(subject)

f.close()
f=open("open.txt","r")
print(f.read())
