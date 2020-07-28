#!/usr/bin/env python
# coding: utf-8

import sys

fastafileloc = sys.argv[1]

def fasta_to_dict(fastafileloc):
    ''' Takes in FASTA data and returns a dict with name, seq, and holder for GC content'''
    with open(fastafileloc, 'r' ) as f:
        seq_list = ''.join(f.readlines()).lstrip('>').split('>')
    
    seq_dict = {}
    
    for element in seq_list:
        element = element.split('\n',1)
        seq_dict[element[0]] = (element[1].replace('\n', ''), {'GC Content': 0})
        
    return seq_dict


def gc_content(seq):
    nuc = {
    'A': 0,
    'T': 0,
    'G': 0,
    'C':0,
    'length': 0,
    'GC Content': 0}

    for i in seq:
        nuc[i] += 1
    
    nuc['length'] = len(seq)
    nuc['GC Content'] = ((nuc['G'] + nuc['C']) / nuc['length'] ) * 100
    
    return (nuc['GC Content'], nuc)
    

seq_dict = fasta_to_dict(fastafileloc)


for k,v in seq_dict.items(): #can combine the dictionary iterations if needed
    v[1]['GC Content'] = gc_content(v[0])[0]


for k,v in seq_dict.items():
    mx = 0
    if v[1]['GC Content'] > mx:
        mx = v[1]['GC Content']


for k,v in seq_dict.items():
    if mx == v[1]['GC Content']:
        print (k,v[1]['GC Content'] )




