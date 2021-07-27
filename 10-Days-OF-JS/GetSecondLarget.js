function getSecondLargest(nums) {
    if(nums.length < 1) {
        return null;
    }
    nums.sort((a, b) =>  b - a)
    return nums[1]
}

/**
 * Complexity O(n)
 * Logic : Iterating over each element in array and we have two variables which holds the largest and second
 * largest values in array. here we are providing condition among this iteration and setting these values
 * accordingly
 * 
 * @param {*} nums 
 */
function getSecondLargestAlgo(nums) {
    let largestNum = -1;
    let secondLargestNum = -1;
    // Iterating over each element
    nums.forEach(element => {
        // Checking if current element is greater than or equal to largestNum. 
        if(element >= largestNum){
            // Extra if condition checking if any iterator element is greater than largest and secondLargest
            // then we need to swap the places with largest as secondLargest and current iterator value as 
            // largest variable
            if(element > largestNum && element > secondLargestNum) {
                secondLargestNum = largestNum
            }
            largestNum = element
        } else if(element >= secondLargestNum) {
            // setting up second largest number if current iterator value is between largest and current
            // secondLargestNum
            secondLargestNum = element
        }
    });
    return secondLargestNum
}

lar = 6,
sec = 5
ele = 10

function main() {
    console.log(getSecondLargestAlgo([1, 0]));
}

/**
 * steps
 * 1) set variables largest, secondLargest
 * 2) loop over array
 * 3) set first variable as largest
 * 4) compare next variable with largest
 * 5) if next variable is greater than largest, then compare it with set it as largest and current variable as secondLargest
 * 6) if next variable is smaller than largest, set it as secondLargest and current variable as largest
 * 
 */

main()