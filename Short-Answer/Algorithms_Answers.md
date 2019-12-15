#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 0(n) because we only run 1 operation and we loop through our operation n times

b)0(n^2) because we have a nested operation a while loop within a for loop (O)

c)Though we're invoking a function within a function 0 complexity would still be 0(n)

## Exercise II

1. start from the middle floor and drop an egg
2. if egg breaks, go to middle floor between current floor and bottom floor and drop an egg
3. if it doesn't break, go to middle floor between current and top floor and drop an egg
4. repeat 2 and 3 until egg breaks from current floor



The formula loops through the floors until it finds the lowest floor that breaks the egg, while the number of floors, n, is divided in half at each iteration. The complexity is log time, or O(log n)
