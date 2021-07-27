function reverseString(s) {
    try{
        let split = s.split("")
        let reverse = split.reverse()
        let join = reverse.join("")
        console.log(join)
    }
    catch(err){
        console.log(err.message)
        console.log(s)
    } finally{
        console.log("Finally block executed")
    }
}

function main() {
    reverseString(123);
}

main()