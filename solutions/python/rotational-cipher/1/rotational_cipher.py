def rotate(text, key):
    alph_lower = 'abcdefghijklmnopqrstuvwxyz'
    alph_upper = alph_lower.upper()
    cypher_alph = ''
    alph_length = 26
    for c in text:
        if c.isalpha():
            alph = alph_upper if c.isupper() else alph_lower
            c_index = alph.index(c)
            new_index = c_index + key
            if new_index >= alph_length:
                new_index -= alph_length
            cypher_alph += alph[new_index]
        else:
            cypher_alph += c
    return str(cypher_alph)