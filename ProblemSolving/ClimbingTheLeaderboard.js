"use strict"
let scores = [1]
let alice = [1,1]
function getRank(scores,alice){
    //Gets Unique values from scores
    let uniqScores = Array.from(new Set(scores));


    let result = []
    
    alice.sort(function(a, b){return a - b}); //Sort alice score in ascending order incase in not sorted.

    let i = uniqScores.length
    for(let value in alice){
        //Condition handle that if alice scored max score than all scores.
        if(alice[value] > uniqScores[0]){
            result.push(1)
            continue
        }
        //loop over the score
        while(i > 0){
            //Add into result when alice score is equal to current iteration score.
            if(alice[value] == uniqScores[i - 1]){
                result.push(i)
                break
            }
            //Add into result when alice score is less than current iteration.
            if(alice[value] < uniqScores[i - 1]){
                result.push(i + 1)
                break
            }
            //Move to next score if none of condition is satiesfies
            i--
        }
    }
   return result
    
}

function uniq(a) {
    return Array.from(new Set(a));
 }

 
console.log(uniq(scores))
console.log(getRank(scores,alice))