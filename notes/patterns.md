# Patterns and Thought Process

## Contains Duplicate 4/17/2026
Given an array of ints, does it contain duplicate values?
- Must make sure same index isn't checked for example nums[0] == nums[0] is always true(I think)
- This can be brute forced with two loops however O(n^2)
- You can use a Hashset as well
### Pattern
- Arrays and Hashing if mentioned usually require iterating through
- Some key words I noticed are 'seen', 'contain', and 'more than once'
- When dealing with "does this exist?" usually hashsets are fastest.

### Brute Force
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
## Two Sum Integer 4/18/2026
Given an array of integers, check if the sum of two numbers in the array == target
### Pattern
- Array of values
- Return indices of the values

### Brute Force
Same as "Contains Duplicate", use a nested loop to iterate through and sum the numbers and check if equals the target. 

### Hash
We use a hashmap which helps us have an instant lookup. The key here is that we can immediatly search up the value needed by doing diff=target-num. if this value is in our hashmap we return [position of diff, current index]. In order to do this properly though we have to make use of enumerate. The way enumerate works is by turning the list into key value pairs. index : value. This is key for Hashmaps!
So we initialize a hashmap, iterate through the values and calculate the diff. if diff in hashmap return small index, curr index. if not there then add the current index into the hashmap by linking the num to the current index. 
- hashmap[ number ] returns index
- hashmap[ num ] = i is different than hashmap[ i ] = num. It changes the key value pair. Must rmr this depending on whats needed, and what return!

