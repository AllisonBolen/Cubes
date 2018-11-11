import sys, math

def main():
    cubeInfo = parseInput() # parse input
    for info in range(0, len(cubeInfo)):
        cubeA, nCubes = volumeofCubeA(cubeInfo[info])
        fillCubeCount = calculateCubes(cubeA, nCubes)
        print(fillCubeCount)
        print()
        fillCubeCount = 0

def calculateCubes( cubeA, nCubes):
    '''
    params:
        cubeA: the volume of the cube we are filling
        nCubes: the list of cubes we are filling cube A with
        fillCubeCount:  starts as zero and as we subtract cube volumnes from cube A we add to This
    return:
        -1 if we cant fill cube A
        fillCubeCount if we did fill cube A
    '''
    # go backwards through the list to subtract the maximum cube sizes first
    # this will minimize the number of cubes it takes to fill cube A
    if cubeA == 0: # the cube is not fillable because it dosent take up space
        return -1
    fillCubeCount = 0
    for cube in range(len(nCubes)-1, -1, -1):
        volumeOfCubeN = pow(pow(2,cube),3)
    # continue subtracting values when we still have space left in Cube A and we still have cubes in to subtract with
    # and the volume of cube N is not zero and the volume of cube N is less than the volume of cube A
        while(cubeA >= 0  and nCubes[cube] > 0 and nCubes[cube] != 0 and volumeOfCubeN <= cubeA):
            # print("cubeA: " + str(cubeA) + " - volume of cube at " +str(cube)+ " where the volume is " + str(pow(pow(2,cube),3)))
            cubeA = cubeA - volumeOfCubeN
            nCubes[cube] = nCubes[cube] - 1
            fillCubeCount = fillCubeCount + 1
    if cubeA > 0: # we did not fill the cube all the way
        return -1
    return fillCubeCount

def volumeofCubeA( listOfCubes ):
    '''
    this calculates the volume of cube A, or the cube we are trying to fill
    returns the volume of cube A and the list of cubes N without cube A's dimensions
    ex:

    '''
    #      length           * width            * height          , [x, y, ... z]
    return listOfCubes[0] * listOfCubes[1] * listOfCubes[2], listOfCubes[3:]


def parseInput():
    '''
    This function checks for command line input or standard in for file information
    and converts it into a line by line list,
    I am going to assume for now that only valid files will be used.
    returns a list of all cube data
    '''
    lines = ""

    # command line input
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as file:
            lines = [l.strip() for l in file]

    # sdandard in
    else:
        lines = sys.stdin.readlines()
        lines = [l.strip() for l in lines]

    # make it a list of integers and strip spaces
    actual = []
    for item in range(0, len(lines)):
        temp = lines[item].split(" ")
        temp = list(map(int, temp))
        actual.append(temp)

    return actual
if __name__ == "__main__": main()
