https://github.com/ElijahMcKay/Sprint-Challenge--Algorithms.git#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3)

The number of times that the loop has to run is n^3 (written in this example `n * n * n`).  The operation inside the while loop is just an operation in constant time, so that doesn't effect the time complexity.

if n = 10, we loop 1000 times
if n = 11, we loop 1331 times
if n = 12, we loop 1728 times


b) O(n^2) complexity.  For every piece of data input in to the algorithm, it has to be looped over twice.  

n____loops_
2     4
4     16
5     32
6     64


c) O(n)

For every n that is added, the function is executing 1 more time.  It decrements each time and has 1 call per call, so when it hits 0 we would have executing the function n times.  Since all of the operations in the function are O(1), this is still linear time.

## Exercise II


