import re

def is_isogram(string):
    regex = "[a-z]"
    string = string.lower()
    for count, char in enumerate(string):
        if re.match(regex, char):
            if len(re.findall(char, string)) > 1:
                return False
    return True
