
EXERCISE 1

1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature

def reading_estimator(filename):

    """reads from a file and estimates the reading time 

    Parameters: (list all parameters and their types)
        the filename of a text file in the same folder

    Returns: (state the return value and its type)
        a time value in mins estimating reading time

    Side effects: (state any side effects)
        throw errors if fed non-text file 
    """
    pass 

3. Create Examples as Tests

# EXAMPLE

"""
If a filename is given that is not a string an exception is thrown.
"""
filename_is_string("filename") => Exception

"""
If a filename is given that doesn't correspond to a textfile an exception is thrown.
"""
file_is_textfile("filename) => Exception

"""
If a filename is given that doesn't correspond to a textfile in the same folder as exception is thrown.
"""
file_is_in folder("filename) => Exception

"""
Given a filename corresponding to a text file in the same folder there is a return.
"""
filename_is_textfile("filename") => any return

"""
Given a textfile filename input the function returns the estimated reading time in minutes. Test 1 - long text (>1min).
"""
estimated_reading_time_long("filename") => String describing time in minutes

"""
Given a textfile filename input the function returns the estimated reading time in minutes. Test 2 - short text (<1min).
"""
estimated_reading_time_short("filename") => String describing time in minutes








EXERCISE 2

Describe the Problem:

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

Design the Function Signature:

-basic_grammar_checker()
-takes a string as a parameter
-returns a boolean 

Create Examples as Tests:

- adds a full stop if there is no puncutation at the end
basic_grammar_checker("Hello world") => "Hello world."

-correctly capitalises first letter if input is lower case
basic_grammar_checker("hello world.") => "Hello world." 

- does nothing and just returns the string if sentence starts with capital letter and ends in suitable sentence-ending punctuation mark
basic_grammar_checker("Hello world.") => "Hello world."

- works with non full stop sentence ending punctuation
basic_grammar_checker("Hello world!) => "Hello world!"

-adds capital first letter AND puncutation if both are missing
basic_grammar_checker("hello world") => "Hello world."

Implement the behaviour: