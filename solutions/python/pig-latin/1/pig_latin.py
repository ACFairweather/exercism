def translate(text):
    words = text.split()
    return ' '.join(translate_word(word) for word in words)

def translate_word(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    rule1prefixes = ['xr', 'yt']

    for prefix in vowels + rule1prefixes:
        if text.startswith(prefix):
            return text + 'ay'

    print (text)

    if 'qu' in text:
        quIndex = text.find('qu')
        if all(text[i] not in vowels for i in range(quIndex)):
            return text[quIndex + 2:] + text[:quIndex + 2] + 'ay'
        
    
    print (text)

    first_vowel_index = None
    for i, c in enumerate(text):
        if c in vowels or c == 'y' and i != 0:
            first_vowel_index = i
            break
    
    if first_vowel_index is not None and text[first_vowel_index] == 'y':
        return text[first_vowel_index:] + text[:first_vowel_index] + 'ay'


    for i, c in enumerate(text):
        if c in vowels:
            return text[i:] + text[:i] + 'ay'

    print(text)
    return text


    