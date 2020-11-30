from DNAToolkit import *
import random
from utilities import colored

randDNAstr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])

inputDNA = ''

DNAstr = (ValidateSeq(randDNAstr))

print(f'\nSequence: {colored(DNAstr)}\n')
print(f'[1] + Sequence Length: {len(DNAstr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAstr)}\n')

print(f'[3] + DNA/RNA Transcription: {transcription(DNAstr)}\n')

print(f"[4] + DNA String + Reverse Complement:\n'5 {DNAstr} 3'")
print(f"   {''.join(['|' for c in range(len(DNAstr))])}")
print(f"3' {reverse_complement(DNAstr)} 5'\n")

print(f'[5] + GC Content: {GCcontent(DNAstr)}%\n')
print(
    f'[6] GC Content in Subsection k=5: {gc_content_subset(DNAstr, k=5)}\n')

print(
    f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAstr, 0)}\n'
)

print(
    f'[8] + Codon frequency (L): {codon_usage(DNAstr, "L")}\n'
)

print('[9] + Reading_frames')
for frame in gen_reading_frames(DNAstr):
    print(frame)

print('\n[10] + Proteins from reading frames')
for frame in gen_reading_frames(DNAstr):
    print(proteins_from_rf(frame))

print('\n[11] + All prots in 6 opening reading frames:')
for prot in all_proteins_from_orfs(NM_000207_3, 0, 0, True):
    print(f'{prot}')