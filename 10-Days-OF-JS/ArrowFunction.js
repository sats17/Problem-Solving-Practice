function modifyArray(nums) {
    return nums.map(n => {
        return n%2==0 ? n*2: n*3;
    })
}

console.log(modifyArray([1,4,3,2]))