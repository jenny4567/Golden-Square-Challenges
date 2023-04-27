from os.path import exists

def reading_estimator(filename):
    if type(filename) != str:
        raise Exception("Filename should be a string.")
    if filename[-3:] != ".md":
        raise Exception("Filename does not correspond to text file.")
    file = "/Users/MakersAdmin/Documents/my_python_code/GoldSquareProjects/Golden_Square_Challenges/lib/" + filename
    if exists(file):
        text = open(file).read()
        #print(text)
        num_words = len(text.split(" "))
        time = round(num_words/200)
        return f"Estimated time: {time} mins"
    else:
        raise Exception("Filename does not correspond to file in same folder.")