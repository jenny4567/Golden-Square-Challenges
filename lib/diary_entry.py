class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string


    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.read_chunk = []

    def count_words(self):
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        return (self.count_words())/wpm

    def reading_chunk(self, wpm, minutes):
        self.words = self.contents.split()
        if self.read_chunk == []:
            chunk = self.words[:wpm * minutes]
            print(chunk)
            self.read_chunk.append(chunk)
        else:
            chunk_length = len(self.read_chunk)
            chunk = self.words[chunk_length:(wpm * minutes)+ chunk_length]
            print(chunk)
        return " ".join(chunk)