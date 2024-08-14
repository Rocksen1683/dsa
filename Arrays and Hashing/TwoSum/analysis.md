# Analysis of Two Sum 
## Naive Solution 
A brute force solution to Two Sum would be having a nested loop to go through each possible pair in the array - resumlting in a time complexity of `O(n^2)`. After going through each pair, we can determine the solution by checking if the sum of the outer and inner loop is equal to the target.
## Optimal Solution 
One optimal solution would be to use a hashmap that keeps track of all of the elements that we visit along with their respective index. With this method, we can eliminate the nested loop giving us a time complexity of `O(n)`