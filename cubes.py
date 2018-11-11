import sys

def main():
    print(main)
    inputFile = sys.argv[1]
    parseInput(inputFile)

def parseInput(inputFile):
    '''
    This function takes file input and converts it into line by line list,
    I am going to assume for now that only valid files will be used.
    '''
    x =""
    with open(inputFile, encoding="utf-8") as file:
        x = [l.strip() for l in file]

    return x
if __name__ == "__main__": main()
