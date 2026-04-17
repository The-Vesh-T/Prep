# Patterns and Thought Process

## Contains Duplicate
Given an array of ints, does it contain duplicate values?
- Must make sure same index isn't checked for example nums[0] == nums[0] is always true(I think)
- This can be brute forced with two loops however O(n^2)
- You can use a Hashset as well
### Pattern
- Arrays and Hashing if mentioned usually require iterating through
- Some key words I noticed are 'seen', 'contain', and 'more than once'
- When dealing with "does this exist?" usually hashsets are fastest.

### Brute force
The brute force method can be thought of as using two place holders lets say A and B. Placeholder A stays on the current index so at the start index 0, while placeholder B stays one step ahead at index_A+1. Placeholder B would then iterate from its starting position to the end of the loop which would check for all instances of a duplicate. 
Must not start at same index, should also have a safety for if placeholder A gets to index-1 because then placeholder B would be out of scope.

Because this solution requires two loops, each of which require O(n) time, the total runtime is O(n^2) which is ineffecient.

### HashSet
A Hashset, or just set, hold values that must be unique. The thing that makes it better than lists is that sets have O(1) lookup time while lists obviously have O(n). 
Since we are given a list of ints, we can use a set by:
- Initialize set
- Iterate through the int array
- Check if the num is in the set, if so return True, else add num to set!

Theoretically you can also make it more compact by checking the size of the set vs original list.
Since sets not allowed dupes if its shorter than original list, there must be a dupe.

-------------------------------------------------------------------------------------------------------------------------------------------------
## Two Sum Integer



