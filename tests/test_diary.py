from lib.diary import *

'''
Test all function with empty diary.
'''
def test_empty_diary():
    my_diary = Diary()
    assert my_diary.all() == []