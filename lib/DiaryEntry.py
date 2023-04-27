class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        self.title = title
        self.contents = contents
        self.words = self.contents.split()
        self.read_chunk = []

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        if isinstance(self.contents,str):
            return f'Number of words: {len(self.words)}'
        else:
            raise Exception("Not a string!")

    def reading_time(self, wpm):
        if type(wpm) != int:
            return "The words per minute parameter must be an integer"
        elif type(self.contents) != str:
            return "The text parameter must be a string"
        else: 
            words = len(self.contents.split())
            minutes = words/wpm
            return round(minutes, 2)

    def reading_chunk(self, wpm, minutes):
        if self.read_chunk == []:
            chunk = self.words[:wpm * minutes]
            print(chunk)
            self.read_chunk.append(chunk)
        else:
            chunk_length = len(self.read_chunk)
            chunk = self.words[chunk_length:(wpm * minutes)+ chunk_length]
            print(chunk)
        return chunk[0]