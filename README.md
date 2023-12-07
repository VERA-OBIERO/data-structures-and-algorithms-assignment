# data-structures-and-algorithms-assignment

This repository contains Python functions  solutions for common tasks related to data structures such as stacks, sequences (lists/tuples), and dictionaries.

## Functions Included

### Stacks:

#### 1. `is_balanced(expression)`
- Determines whether a given expression containing parentheses, curly braces, and square brackets is balanced or not.

### Sequences (Lists/Tuples):

#### 2. `remove_duplicates(sequence)`
- Removes duplicates from a sequence (list or tuple) while maintaining the original order of elements.

### Dictionaries:

#### 3. `word_frequency(sentence)`
- Calculates the frequency of each word in a sentence, ignoring punctuation and considering words in a case-insensitive manner.

## Setup instructions

To use these functions:

1. Clone the repository or copy the functions into your Python environment.

2. Import the functions into your Python script or interactive session using:
    ```python
    from data_structures_functions import is_balanced, remove_duplicates, word_frequency
    ```

3. Use the functions as needed. Examples:
    ```python
    # Stacks
    expression1 = "([]{})"
    expression2 = "([)]"
    print(is_balanced(expression1))  # Output: True
    print(is_balanced(expression2))  # Output: False

    # Sequences
    input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = remove_duplicates(input_sequence)
    print(result)  # Output: [2, 3, 4, 5, 6, 7]

    # Dictionaries
    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    print(result)
    ```
