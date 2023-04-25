from os.path import exists

def reading_estimator(filename):
    if type(filename) != str:
        raise Exception("Filename should be a string.")
    if filename[-3:] != ".md":
        raise Exception("Filename does not correspond to text file.")
    if exists("/Users/MakersAdmin/Documents/my_python_code/GoldSquareProjects/Golden_Square_Challenges/lib/" + filename):
        text = open(filename).read()
        print(text)
    else:
        raise Exception("Filename does not correspond to file in same folder.")