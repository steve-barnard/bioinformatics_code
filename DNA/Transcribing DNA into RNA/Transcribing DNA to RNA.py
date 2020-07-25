#!/usr/bin/env python
# coding: utf-8

# In[1]:
import sys

def transcribe_to_rna(dnafile):
    ''' transcribes rna complement from dna input'''
    with open (dnafile, 'r') as f:
        seq = f.readlines().rstrip('\n')
    
    return seq.replace('T','U')

transcribe_to_rna('rosalind_rna.txt')
