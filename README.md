# Cubes

### How To:
What you need to run it:
0. Clone repo
1. Have python3 installed
2. I have configured multiple ways for you to run this script:
    * ./runner problems.txt
    * python3 cubes.py problems.txt
    * python3 cubes.py < problems.txt
3. You can run the unit test file using:
    * ./test.sh
    * python3 cubeTests.py

---

### Programming test:
In the classic computer science textbook "The Structure and Interpretation of Computer Programs" (Abelson & Sussman, 1984), the authors write: `"Thus, programs must be written for people to read, and only incidentally for machines to execute"`, so keep that in mind when implementing your solution.
 
This solution uses Python3 for the meat of the solution and bash scripting for user friendly running.

---

You are given a box with integer dimensions length x width x height. You
also have a set of cubes whose sides are powers of 2, e.g. 1x1x1, 2x2x2,
4x4x4 etc.
You need to fill the box with cubes from the set.
Write a program that for a given box and given set of cubes can determine
the smallest number of cubes needed to fill the box.
The set of cubes can be represented for instance as a list or array of
numbers, where the position in the list designates the dimension of the
cube. E.g. 100 10 1 means you have 100 cubes of 1x1x1 and 10 cubes of 2x2x2
and 1 cube of 4x4x4.
A problem specification is a sequence of lines separated by newline. Each
line has the box dimensions as the first three elements and the remaining
elements enumerate the given cubes. Elements are separated by a single
space. Lines are terminated by your platform’s newline convention. E.g.
2 3 4 5 6
7 8 9 1 2 3 4
specifies two problems:
a box with dimensions 2 x 3 x 4, 5 cubes of 1x1x1 and 6 cubes of 2x2x2
a box with dimensions 7 x 8 x 9, 1 cube of 1x1x1, 2 of 2x2x2, 3 of 4x4x4, and 4 of 8x8x8.
Your program should read one or more problem specifications from stdin and
print the answer to each problem on stdout. Spend as little effort as
possible on parsing and validation of the input. An unsolvable problem
should yield -1. Please provide instructions on how to run / compile your
program.
Examples:
Assume the file ‘problems.txt’ contains:
10 10 10 2000

10 10 10 900

4 4 8 10 10 1

5 5 5 61 7 1

5 5 6 61 4 1

1000 1000 1000 0 0 0 46501 0 2791 631 127 19 1

1 1 9 9 1

Then executing
./myprogram < problems.txt
should print the following to stdout:
1000

-1

9

62

59

50070

9

---
### Approach:

I think that this could be done by calculating the volume of the initial cube (Cube A) and then keeping track of the volume of the cubes (Cube N) we want to fill cube A with.

Given: a 10x10x10 cube A with a volume of w*l*h = 1000 units^3. With a list of cubes denoted by [b,c, ..., z] where the index of the cube in the list determines the volume the cube 2^(list index of b,c,...,z) and the value at that index is the number of cubes with that volume.

We can find the total number of cubes that fit in cube A by subtracting cube at N's volume from cube A's volume to see if that cube will fit. Once cube A's volume is zero we can no longer fit other cubes in cube A and thus we end the sequence.
---
### Testing
Edge cases:
1. No cubes listed will fit Cube A
2. Cubes listed will fit but not fill Cube A
3. Cube A is zero volume
4. ...
Coverage of edge cases can be seen in the cubeTests.py file
