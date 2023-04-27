from lib.diary_entry import *
from lib.diary import *

'''
Tests adding a diary entry to a diary.
Requires: diary entry to initiate, diary all & add function to work.
'''
def test_add_entry_to_diary():
    my_diary = Diary()
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    my_diary.add(my_first_entry)
    assert my_diary.all() == [("First Day", "I love my diary!")]


'''
Tests adding multiple diary entries to a diary.
Requires: diary entry to initiate, diary all & add function to work.
'''
def test_add_multiple_entries_to_diary():
    my_diary = Diary()
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    my_diary.add(my_first_entry)
    my_second_entry = DiaryEntry("Second Day", "Got takaway today.")
    my_diary.add(my_second_entry)
    my_third_entry = DiaryEntry("Third Day", "I have lots of time to write today, so I will write loads.")
    my_diary.add(my_third_entry)
    assert my_diary.all() == [("First Day", "I love my diary!"), ("Second Day", "Got takaway today."),("Third Day", "I have lots of time to write today, so I will write loads.")]

'''
Tests count_words function of diary for multiple diary entries.
Requires: diary entry count_words method to work.
'''
def test_word_count_of_diary():
    my_diary = Diary()
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    my_diary.add(my_first_entry)
    my_second_entry = DiaryEntry("Second Day", "Got takaway today.")
    my_diary.add(my_second_entry)
    assert my_diary.count_words() == 7

'''
Tests reading_time function for multiple diary entries.
Requires: diary entry reading_time function
'''
def test_diary_reading_time():
    my_diary = Diary()
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    my_diary.add(my_first_entry)
    my_third_entry = DiaryEntry("Third Day", "I have lots of time to write today, I will write loads.")
    my_diary.add(my_third_entry)
    assert my_diary.reading_time(17) == 1

'''
Tests find_best_entry_for_reading_time for multiple Diary Entries.
Requires: diary reading chunk method
'''
def test_best_entry():
    my_diary = Diary()
    my_first_entry = DiaryEntry("First Day", "I love my diary!")
    my_diary.add(my_first_entry)
    my_second_entry = DiaryEntry("Second Day", "Got takaway today.")
    my_diary.add(my_second_entry)
    my_third_entry = DiaryEntry("Third Day", "I have lots of time to write today, so I will write loads.")
    my_diary.add(my_third_entry)
    assert my_diary.find_best_entry_for_reading_time(36,1) == ("Third Day", "I have lots of time to write today, so I will write loads.")