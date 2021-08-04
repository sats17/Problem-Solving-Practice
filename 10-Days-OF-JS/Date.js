function getDayName(dateString) {
    let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    let dayName;
    // Write your code here
    dayName = days[new Date(dateString).getDay()]
    return dayName;
}

function main(){
    console.log(getDayName("08/04/2021"))
}
main()