def task_checker(string):
    if type(string) != str:
        raise Exception("Not a string!")
    else:
        if "#TODO" in string:
            if len(string) == 5:
                return False
            else:
                return True
        else:
            return False