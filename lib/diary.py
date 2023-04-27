class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        Formatted_Diary = []
        for entry in self.entries:
            Formatted_Diary.append((entry.title, entry.contents))
        return Formatted_Diary 

    def count_words(self):
        total_words = 0
        for entry in self.entries:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        total_time = 0
        for entry in self.entries:
            total_time += entry.reading_time(wpm)
        return round(total_time)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        best_entry = None
        max_words = 0
        for entry in self.entries:
            if entry.reading_chunk(wpm, minutes) == entry.contents:
                if entry.count_words() > max_words:
                    best_entry = entry
                    max_words = entry.count_words()
        return (best_entry.title, best_entry.contents)
        
        