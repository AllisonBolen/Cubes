import sys

def main():
    inputFile = sys.argv[1]
    cubeInfo = parseInput(inputFile)

    for info in range(0, len(cubeInfo)):
        cubeA, nCubes = volumeofCubeA(cubeInfo[info])
        for cube in range(0, len(nCubes)):
            print(nCubes[cube])
    # calculate line by line the cubes that fit
    # for cubes in cubeInfo:



def volumeofCubeA( listOfCubes ):
    '''
    this calculates the volume of cube A, or the cube we are trying to fill
    returns the volume of cube A and the list of cubes N without cube A's dimensions
    ex:

    '''
    print(listOfCubes)
    #      length           * width            * height          , [x, y, ... z]
    return int(listOfCubes[0]) * int(listOfCubes[1]) * int(listOfCubes[2]), listOfCubes[3:]


def parseInput(inputFile):
    '''
    This function takes file input and converts it into line by line list,
    I am going to assume for now that only valid files will be used.
    returns a list of all cube data
    '''
    x = ""
    actual = []
    with open(inputFile, encoding="utf-8") as file:
        x = [l.strip() for l in file]
    for item in range(0, len(x)):
        actual.append(x[item].split(" "))
    return actual
if __name__ == "__main__": main()
