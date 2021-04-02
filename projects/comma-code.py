#! /usr/local/bin/env python3

# comma-code.py

# Say you have a list value like this:

spam = ["apples", "bananas", "tofu", "cats"]

# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted before
# the last item. For example, passing the previous spam list to the function
# would return 'apples, bananas, tofu, and cats'. But your function should be
# able to work with any list value passed to it.


def string(list):
    output = ""
    for i in range(len(list)):
        if i == (len(list) - 1):
            output += "and " + list[i]
        else:
            output += list[i] + ", "
    return output


return_value = string(spam)
print(return_value)
