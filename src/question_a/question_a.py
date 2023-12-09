#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    index = 0

    while index < len(dna_string1):
        position = dna_string1.find(dna_string2, index)
        if position == -1:
            break
        positions.append(position + 1) 
        index = position + 1

    return tuple(positions) 

def validate_string1(dna_string):
    return len(dna_string) > 8 and len(dna_string) <= 16

def validate_substring(dna_substring):
    return len(dna_substring) == 4
