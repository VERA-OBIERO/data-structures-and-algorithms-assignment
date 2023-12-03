import string

def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or mapping[char] != stack.pop():
                return False

    return not stack

def remove_duplicates(sequence):
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def word_frequency(sentence):
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.translate(translator).lower().split()

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency