from lib.basic_grammer_checker import *

def test_no_end_punctuation():
    text = basic_grammer_checker("Hello world")
    assert text == "Hello world."

def test_correctly_capitalises():
    text = basic_grammer_checker("hello world.")
    assert text == "Hello world."

def test_does_nothing():
    text = basic_grammer_checker("Hello world!")
    assert text == "Hello world!"

def test_punc_and_cap():
    text = basic_grammer_checker("hello world")
    assert text == "Hello world."

