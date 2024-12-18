(1)What does "string concatenation" mean?
the process of combining two or more strings into a single string

python
first_name = "Mussa"
last_name = "Baikro"
full_name = first_name + " " + last_name
print(full_name)

Javascript
let firstName = "Mussa";
let lastName = "Baikro";
let fullName = firstName + " " + lastName;
console.log(fullName);


(2)Three rules for creating variable names:
1.Variable names must start with a letter or an underscore. 
2.Variable names can only have letters, numbers, underscores, and dollar signs. 
3.Variable names are case-sensitive. 

(3)Define and provide code examples for the following variable name formats:

1.Camel Case: The first word is lowercase, and every subsequent word starts with an uppercase letter

let myVariableName = "Hello";
console.log(myVariableName);

2.Snake Case: Words are separated by underscores and all letters are lowercase

my_variable_name = "Hello"
print(my_variable_name)

3.Pascal Case: Similar to camel case, but the first letter is also uppercase

let MyVariableName = "Hello";
console.log(MyVariableName);

(4)Find the missing variable for the following code snippets:

Python Version:

a = 3  # the missing variable
b = a * 100
print(b)  # the output should be 300

JavaScript Version:

let a = 7;  // the missing variable
let b = a * 100;
console.log(b);  // the output should be 700

(5)Logical Operators in Python and JavaScript:
Python Version:
In Python, we would use the and logical operator to ensure that both conditions are true. The expression checks if x > 1 and if z == 4.

x = 10
y = 2
z = y * 2

print(x > 1 and z == 4)  # This will print True, because both conditions are true.

(6) JavaScript Version:
In JavaScript, we would use the & logical operator to reflect that the result between the code expressions is false. The expression checks if x <= 12 and if z < 10.

var x = 12;
var y = 2;
var z = 12 / 4;

console.log(x <= 12 && z < 10);  // This will print false, because `z < 10` is false.

