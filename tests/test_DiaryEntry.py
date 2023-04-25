from lib.DiaryEntry import *
entry = DiaryEntry("Tuesday 25th April", "was good enough")

def test_diary_format():
    #entry = DiaryEntry("Tuesday 25th April", "was good enough")
    assert entry.format() == "Tuesday 25th April: was good enough"

def test_count_words():
    assert entry.count_words() == "Number of words: 3"

def test_reading_time():
    assert entry.reading_time(3) == 1

def test_reading_chunk():
    assert entry.reading_chunk(1,1) == "was"

def test_reading_second_chunk():
    assert entry.reading_chunk(1,1) == "good"