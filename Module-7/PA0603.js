let marks = [85, 90, 78, 92, 88]

function calculate(marks) {
    let total = 0;
    for (let i = 0; i < marks.length; i++) {
        total += marks[i];
    }
    return total
}

console.log(calculate(marks));