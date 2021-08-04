function validateName(name){

    const re = /^(Mr?s|[MDE]r)\.[A-Za-z]+$/;
    if(name.match(re)){
        console.log("Name "+name+" Valid")
    } else{
        console.log("Name "+name+" Invalid")
    }
}

validateName("Er .Abc")
validateName("Er.Abc")