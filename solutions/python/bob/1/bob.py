def response(hey_bob):
    output = 'Whatever.'
    trimmed_input = hey_bob.strip()
    if (not trimmed_input):
        output = 'Fine. Be that way!'
    elif (trimmed_input.isupper() and '?' in trimmed_input):
        output = 'Calm down, I know what I\'m doing!'
    elif (trimmed_input[len(trimmed_input) - 1] == '?'):
        output = 'Sure.'
    elif (trimmed_input.isupper()):
        output = 'Whoa, chill out!'
    return output