"""
#rstrip --> removes blank space if any


"""

def main():
    rev=[]
    with open("ReverseEachWord.txt") as fh:
        for i in fh:
            word_list= i.rstrip().split(" ")
        for i in word_list:
            rev.append(i[::-1])
        print(" ".join(rev))
        rev.clear()
if __name__ == "__main__":
    main()

