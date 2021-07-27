'use strict';

function factorial(n){
    if(n === 1){
        return 1;
    } else{
        let fact = n * factorial(n - 1);
        return fact;
    }
}

function main() {
    
    console.log(factorial(5));
}

main()