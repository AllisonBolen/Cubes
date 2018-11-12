# Cubes

### How To:
What you need to run it:

0. Clone repo
1. Have python3 installed
2. I have configured multiple ways for you to run this script:
    * ./runner.sh problems.txt
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
**Write a program that for a given box and given set of cubes can determine
the smallest number of cubes needed to fill the box.**
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

**I disagree with the output for this example.**

---
### Why I disagree:

For the above example my program calculates:
1000

-1

9

13

59

50070

2

This differs from the problem statement example on two instances:

1. Instead of 62 for cube info of: `5 5 5 61 7 1`. **I got 13**. I think my answer is correct because we are looking for the
*smallest* number of cubes it takes to fill the box. In this case the volume of the box would be 125 units<sup>3</sup> and we were given 61 cubes of 1 units<sup>3</sup>, 7 cubes of 8 units<sup>3</sup>, and 1 cubes of 64 units<sup>3</sup>.
The reason it should be 13 instead of 62:
We will start by subtracting the largest amount first, this will minimize the number of cubes it takes to fill the box. We will subtract 64 units<sup>3</sup> from 125 units<sup>3</sup> to get 61 units<sup>3</sup> remaining. In other words we just filled our 125 units<sup>3</sup> cube with a 64 units<sup>3</sup> cube and now we have 61 units<sup>3</sup> left to fill. Since we just used up our 1 cube of volume 64 units<sup>3</sup> we then move to the next set of cubes with the largest volume. This would be our set of 7 cubes with 8 units<sup>3</sup> of volume. For this one we will see how many volume units of 8 can fit into 61 by using subtraction. We will subtract 8 until we either run out of cubes with this volume or until we can no longer fit 8 units<sup>3</sup> into the box. We find that 8units<sup>3</sup> fits in 61units<sup>3</sup> 7 times. So now we have used 8 cubes to fill our box with 5 units<sup>3</sup> left to fill. We will then use 5 of our 61 1 units<sup>3</sup> cubes to fill the remaining space. This leaves us with having used 13 cubes to fill the box, while minimizing the number of cubes it takes to fill the box.
A way you could get 62 cubes as the answer for this example would be if you replaced the 7 cubes of 8 units<sup>3</sup> with 0 cubes of 8 units<sup>3</sup>. Then you would have 125 units<sup>3</sup> minus 64 units<sup>3</sup> leaving 61 units<sup>3</sup> left to be filled. With the remaining space in the box you could use all 1 of your 1 units<sup>3</sup> to completely fill the box thus resulting in 62 cubes being used.

2. Instead of 9 cubes for cube info of `1 1 9 9 1`. **I got 2**. I think my answer is correct because we are looking for the
*smallest* number of cubes it takes to fill the box. In this case the volume of the box would be 9 units<sup>3</sup> and we were given 9 cubes of 1 units<sup>3</sup>, 9 cubes of 8 units<sup>3</sup>, and 1 cube of 64 units<sup>3</sup>.
The reason it should be 2 instead of 9:
We will start by subtracting the largest amount first, this will minimize the number of cubes it takes to fill the box. We will subtract 8 units<sup>3</sup> from 9 units<sup>3</sup> to get 1 units<sup>3</sup> remaining. In other words we just filled our 9 units<sup>3</sup> cube with a 8 units<sup>3</sup> cube and now we have 1 units<sup>3</sup> left to fill. Since we just used up our one of our 9 cubes of volume 8 units<sup>3</sup> we now have 8 cubes of 8 units<sup>3</sup>. We can no longer fit cubes of 8 units<sup>3</sup> into the space remaining in the box so we then move to the next set of cubes with the largest volume. This would be our set of 9 cubes with 1 units<sup>3</sup> of volume. For this one we will see how many volume units of 1 can fit into 1 by using subtraction. We will subtract 1 until we either run out of cubes with this volume or until we can no longer fit 1 units<sup>3</sup> into the box. We find that 1units<sup>3</sup> fits in 1units<sup>3</sup> 1 time. So now we have used 1 cubes to fill our box with 0 units<sup>3</sup> left to fill. This leaves us with having used 2 cubes to fill the box, while minimizing the number of cubes it takes to fill the box.
A way you could get 9 cubes to fill the box would be if you did not have any cubes of 8 units<sup>3</sup> and only have cubes of 1 units<sup>3</sup>. Then it will take 9 cubes of 1 units<sup>3</sup> to fill the box.

All other output for the example matched what I calculated and I could not find a better way to minimize those results.

---

### Approach:

I think that this could be done by calculating the volume of the initial cube (box) and then keeping track of the volume of the cubes we want to fill box with.

Given: a 10x10x10 box with a volume of w*l*h = 1000 units^3. With a list of cubes denoted by [b,c, ..., z] where the index of the cube in the list determines the volume the cube 2^(list index) and the value at that index is the number of cubes with that volume.

We can find the total number of cubes that fit in the box by subtracting cube at N's volume from the box's volume to see if that cube will fit. Once the box's volume is zero we can no longer fit other cubes in the box and thus we end the sequence.

---

### Testing
Edge cases:
1. No cubes listed will fit the box
2. Cubes listed will fit but not fill the box
3. The box is zero volume
4. ...

Coverage of edge cases can be seen in the cubeTests.py file
