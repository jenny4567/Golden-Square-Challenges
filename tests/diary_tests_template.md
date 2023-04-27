 # File: test_diary_integration

'''
Tests adding a diary entry to a diary.
Requires: diary entry to initiate, diary all & add function to work.
'''
my_diary = Diary()
my_first_entry = DiaryEntry("First Day", "I love my diary!")
my_diary.add(my_first_entry)
my_diary.all() => ("First Day", "I love my diary!")

'''
Tests count_words function of diary for multiple diary entries.
Requires: diary entry count_words method to work.
'''
my_diary = Diary()
my_first_entry = DiaryEntry("First Day", "I love my diary!")
my_diary.add(my_first_entry)
my_second_entry = DiaryEntry("Second Day", "Got takaway today.")
my_diary.add(my_second_entry)
my_diary.count_words() => 7

'''
Tests reading_time function for multiple diary entries.
Requires: diary entry reading_time function
'''
my_diary = Diary()
my_first_entry = DiaryEntry("First Day", "I love my diary!")
my_diary.add(my_first_entry)
my_second_entry = DiaryEntry("Second Day", "Got takaway today.")
my_diary.add(my_second_entry)
my_diary.reading_time() => ??

'''
Tests find_best_entry_for_reading_time for multiple Diary Entries.
Requires: diary reading time method
'''
my_diary = Diary()
my_first_entry = DiaryEntry("First Day", "I love my diary!")
my_diary.add(my_first_entry)
my_second_entry = DiaryEntry("Second Day", "Got takaway today.")
my_diary.add(my_second_entry)
my_third_entry = DiaryEntry("Third Day", "I have lots of time to write today, so I will write loads.")
my_diary.add(my_third_entry)
my_diary.find_best_entry_for_reading_time() => [decide wpm etc to check each]

  # File: test_diary

'''
Test all function with empty diary.
'''
my_diary = Diary()
my_diary.all() => None


   # File: test_diary_entry

'''
Tests diary entry initiation.
'''
my_first_entry = DiaryEntry("First Day", "I love my diary!")
my_first_entry.title => "First Day"
my_first_entry.contents => "I love my diary!"

'''
Tests count_words method
Requires: above
'''
my_first_entry = DiaryEntry("First Day", "I love my diary!")
my_first_entry.count_words() => 4

'''
Tests reading_time method
Requires: both above
'''
my_first_entry = DiaryEntry("First Day", "I love my diary!")
my_first_entry.reading_time() => ??

'''
Tests reading_chunk
'''
my_first_entry = DiaryEntry("First Day", "I love my diary!")
my_first_entry.reading_time(2,1) => "I love"
my_first_entry.reading_time(2,2) => "I love my diary!"
my_first_entry.reading_time(1,2) => "I love my diary!"
