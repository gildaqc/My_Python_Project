import argparse
from Bio import SeqIO
from Bio.Seq import Seq

def find_rframes(sequence, min_length):
    rframes = []
    seq_len = len(sequence)

    for strand, seq in [(+1, sequence), (-1, sequence.reverse_comple>
        for frame in range(3):
            for start in range(frame, seq_len, 3):
                if seq[start:start+3] == 'ATG':  # Start codon
                    for end in range(start + 3, seq_len, 3):
                        if seq[end:end+3] in ['TAA', 'TAG', 'TGA']: >
                            rframe = seq[start:end+3]
                            if len(rframe) / 3 >= min_length:  # Che>
                                rframes.append((start, end+3, strand>
                            break
    return rframes

def main(input_file, min_length):
    for record in SeqIO.parse(input_file, "fasta"):
        sequence = record.seq
        rframes = find_rframes(sequence, min_length)
        for start, end, strand, rframe in rframes:
            strand_symbol = '+' if strand == 1 else '-'
            print(f">ORF_{start}_{end}_{strand_symbol}")
            print(rframe)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find ORFs in a FAS>
    parser.add_argument("input_file", help="Input FASTA file")
    parser.add_argument("-l", "--min_length", type=int, default=100,
                        help="Minimum ORF length in codons (default:>
    args = parser.parse_args()
    main(args.input_file, args.min_length)
