#!/usr/bin/env python
# coding: utf-8

# In[2]:


with open('rosalind_dna.txt', 'r') as f:
    seq = f.readline().rstrip('\n')

nuc = {
    'A': 0,
    'T': 0,
    'G': 0,
    'C':0
}

for i in seq:
    nuc[i] += 1

print ( nuc['A'],nuc['C'],nuc['G'],nuc['T'], )


# In[ ]:




