import sys

file_input = sys.argv[1] #0 is the command to run script 1 is the file to use for input

with open(file_input, 'r') as f:
    seq, motif = [i.rstrip('\n') for i in f.readlines()]

def findMotif(seq, motif):
    '''Takes a DNA seq and a DNA motif and returns locations of the motif in the DNA seq indexed at 1'''
    len_motif = len(motif)
    len_seq = len(seq)
    motif_locs = []
    if len_motif > len_seq:
        raise ValueError("motif be smaller than the seq")
    else:
        for i in range(len_seq - len_motif):
            if seq[i:i+len_motif] == motif:
                motif_locs.append(i+1)
            else:
                pass
    return motif_locs


print(findMotif(seq,motif))