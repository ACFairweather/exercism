def encode(plain_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = []
    for c in plain_text.lower():
        if c.isalpha():
            new_text.append(alphabet[25 - alphabet.index(c)])
        elif c.isnumeric():
            new_text.append(c)
    new_text_string = ''.join(new_text)
    grouped_text = ' '.join([new_text_string[i:i+5] for i in range(0, len(new_text_string), 5)])
    return grouped_text


def decode(ciphered_text):
    backwards_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    new_text = []
    for c in ciphered_text:
        if c.isalpha():
            new_text.append(backwards_alphabet[25 - backwards_alphabet.index(c)])
        elif c.isnumeric():
            new_text.append(c)
    new_text_string = ''.join(new_text)
    return new_text_string
    
    
