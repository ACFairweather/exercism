def to_rna(dna_strand):
    output = ''
    dict = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    for c in dna_strand:
        output += dict[c]
    return output
