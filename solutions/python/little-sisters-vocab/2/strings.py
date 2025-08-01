"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    output = prefix
    for i in range (1, len(vocab_words)):
        output +=  " :: " + prefix + vocab_words[i]
    return output


def remove_suffix_ness(word):
    return word[0:-5] + "y" if (word[-5] == "i") else word[0:-4]


def adjective_to_verb(sentence, index):
    return sentence[:-1].split()[index] + "en"
