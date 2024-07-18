#### so finding a target in a list and returning its index

### Steps
define naive search and binary search 
for bianry search get a low and high so recursion works properly
and a midpoint obvs
and then check for lower and higher than midpoint

for the comparison and timing, create a random set, then sort it into list
and then divide by length so you get the average
and get time obvs 

#
#### binary search vs naive search
binary search is a bit like divide and conquer, uses the fact that the list is sorted
so half the list, it that is the target thats the result, and if not then ask if greater (or smaller) than target

naive search: scan list asking if it is equal to target, if yes return inex, if no, return -1

proving that naive search is slower that binary search
