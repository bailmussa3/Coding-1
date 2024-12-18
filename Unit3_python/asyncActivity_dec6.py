1. 

def revere_word(word):
    return word[::-1]

# Example usge
print(reverse_word("pet")  # Output: 'tep'
print(reverse_word("book")  # Output: 'koob'

2.

def state_landmark(state):
    landmarks = {
        "Pennsylvania": "Liberty Bell",
        "New York": "Statue of Liberty",
        "California": "Hollywood Walk of Fame",
        "Florida": "Disney World"
    }
    
    state = state.title()  # first letters of each word to match our keys

    if state in landmarks:
        return "A landmark in {state} is {landmarks[state]}."
    else:
        return "The state {state} could not be found."

# Example usage
print(state_landmark("Pennsylvania"))  # Output: 'A landmark in Pennsylvania is Liberty Bell.'
print(state_landmark("New York"))  # Output: 'A landmark in New York is Statue of Liberty.'
print(state_landmark("Texas"))  # Output: 'The state Texas could not be found.'

 