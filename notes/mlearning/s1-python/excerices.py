# Dictionary comprehension
{key_expression: value_expression for item in iterable}

# Is EXACTLY equivalent to:
dictionary = {}
for item in iterable:
    dictionary[key_expression] = value_expression
    # Comprehension
squares = {x: x**2 for x in [1, 2, 3, 4]}
# Result: {1: 1, 2: 4, 3: 9, 4: 16}

# Equivalent loop
squares = {}
for x in [1, 2, 3, 4]:
    squares[x] = x**2