
f=open("msg.txt")
def read_file():
    print("Printing each line in the program")

for i in f:
    print(i)
f.close()

def main():
    read_file()

if __name__=="__main__":
    main()