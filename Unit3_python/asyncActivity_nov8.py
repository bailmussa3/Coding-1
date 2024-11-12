a = '?'
b = a * 100  # This will create a string of 100 '?' characters, not a numerical value
print(b)  # This will print 100 '?' characters in a row, not the number 300

a = 3  # Use a number, not a string
b = a * 100  # Now b will be 300, since 3 * 100 = 300
print(b)

let a = '?'
let b = a * b  // Error: b is undefined here
console.log(b)

var x = 12
var y = 2
var z = 12 / 4

console.log(x <= 12 || z < 10)  // false because both conditions are true, but we're testing the case where one would be false
