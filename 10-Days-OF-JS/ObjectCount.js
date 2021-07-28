function getCount(objects) {
    let count = 0
    objects.forEach(element => {
        if(element.x == element.y){
            count++
        }
    });
    return count
}


function main() {
    let objects = [];
    
    objects.push({'x':1, 'y':1})
    objects.push({'x':2, 'y':1})
    objects.push({'x':3, 'y':3})
    objects.push({'x':2, 'y':4})


    console.log(getCount(objects))
}

main()