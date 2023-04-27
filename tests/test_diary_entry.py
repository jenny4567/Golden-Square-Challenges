from lib.diary_entry import *

'''
Tests diary entry initiation.
'''
def test_diary_init():
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    test_outcomes = [my_first_entry.title == "First Day" , my_first_entry.contents == "I love my diary!"]
    assert test_outcomes == [True, True]

'''
Tests count_words method
Requires: above
'''
def test_count_entry_words():
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    assert my_first_entry.count_words() == 4

'''
Tests reading_time method
Requires: both above
'''
def test_reading_time_entry():
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    assert my_first_entry.reading_time(2) == 2

'''
Tests reading_chunk
'''
def test_reading_chunk():
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    my_second_entry = DiaryEntry("Second Day", "Got takaway today.")
    my_third_entry = DiaryEntry("Third Day", "I have lots of time to write today, so I will write loads.")
    chunk_checks = [
        my_first_entry.reading_chunk(2,1) == "I love",
        my_second_entry.reading_chunk(2,2) == "Got takaway today.",
        my_third_entry.reading_chunk(1,2) == "I have"
    ]
    assert chunk_checks == [True, True, True]
    