#!/usr/bin/env python
# coding: utf-8

# In[35]:


import sys

filename = sys.argv[1]
# filename = 'test.txt'

def genComplementDNA(filename):
    ''' Takes in a text file of a 5' to 3' DNA
        and returns a tuple
        (complement strand, original strand)'''

    with open(filename, 'r') as f:
        seq = ''.join(f.readlines()).replace('\n','')

    revStrand = seq[::-1]
    compStrand = ''
    
    for i in revStrand:
        if i== 'A':
            compStrand += 'T'
        elif i == 'T':
            compStrand += 'A'
        elif i == 'G':
            compStrand += 'C'
        elif i == 'C':
            compStrand += 'G'
        else:
            pass
    
    return (compStrand, seq)

complement = genComplementDNA(filename)

print ('Complement Strand: {} \nOriginal Strand: {}'.format(complement[0],complement[1]))

