function Rectangle(a, b) {
    let rectangle = {}
    rectangle.length = a
    rectangle.width = b
    rectangle.perimeter = (2 * a) + (2 * b)
    rectangle.area = a * b
    return rectangle
}


function main() {
    
    const rec = new Rectangle(10, 5);
    
    console.log(rec.length);
    console.log(rec.width);
    console.log(rec.perimeter);
    console.log(rec.area);
}

main()