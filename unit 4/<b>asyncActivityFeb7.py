1.A "FOR" loop is used when you know how many times you want to repeat something, like going through a list. A "WHILE" loop keeps going as long as a condition is true, and you don’t always know how many times it will run.

2.A situation where you would use a WHILE loop is when you want to keep asking the user for a valid input, like a number, until they give the right answer.
python

number = 0
while number != 5:
    number = int(input("Enter the number 5: "))
print("5")
This loop will keep asking the user until they enter the number 5.

3.For the graduation checker program, we can write a function that finds the highest grade in a list. Once it finds the highest grade, it will return a message saying what it is.
python
def find_highest_grade(grades):
    highest_grade = grades[0]  # Start with the first grade
    for grade in grades:
        if grade > highest_grade:
            highest_grade = grade
    return "The highest grade is " + str(highest_grade)


grades = [88, 92, 79, 85, 95]
message = find_highest_grade(grades)
print(message)
This function goes through each grade in the list and finds the highest one.