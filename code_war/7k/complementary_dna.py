# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def DNA_strand(dna):
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    return ''.join(complement[nucleotide] for nucleotide in dna)
