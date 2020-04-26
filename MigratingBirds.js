function calculate(arr){
    let map = {}
    answer = -1
    for(i=0;i < arr.length;i++){
        if(arr[i] in map){
            map[arr[i]] = map[arr[i]] + 1
            continue
        }
        map[arr[i]] = 1
        
    }
    high = -1
    for(key in map){
        if(high > map[key]){
            continue
        }
        high = map[key]  
    }
    for(key in map){
        if(high == map[key]){
            answer = key
            return answer
        }

    }

}

birdsArr = [1,4,2,2,4,4,4,3,3,3]
console.log(calculate(birdsArr))