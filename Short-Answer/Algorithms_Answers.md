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

This is a good use case for binary search.

We can start by going to the halfway point of the building `n // 2`

If the egg breaks dropping form n // 2, we can half that number again.  In other words n // 2 will now be the new "top" of the building. 

If the egg doesn't break for some reason, `n // 2` will be our new "bottom". 

We will repeat this process until we find the floor that the egg doesn't break on.  