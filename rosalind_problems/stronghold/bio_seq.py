from bio_structs import *

class bio_seq:

    def __init__(self, seq='ATCG', seq_type='DNA', label='No label'):
        '''Sequence initialization, validation.'''
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type}"

    # check sequence if DNA string
    def validateSeq(self, dna_seq):
        return set(DNA_Nucleotides).issuperset(self.dna_seq)