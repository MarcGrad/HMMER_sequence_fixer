# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:06:52 2019
Updated on June 10 2019
@author: Marcin Gradowski
"""

import requests as r
from Bio import SeqIO
from io import StringIO
import collections
from itertools import groupby

def result_name_maker(name):
    name_split = name.split('.')
    new_name = name_split[0] + '_fixed.fa'
    return new_name

#FILENAME
filename = 'example.fa'
#WHAT WE WANT TO SKIP LIST
which_sequence_to_skip = ['A0A0G4M2S6_9PEZI']


#read sequences
with open(filename,'r') as rs:
    sequences = list(SeqIO.parse(rs, 'fasta'))
     
    #sequence container to which we will add
    sequences_fasta = []
    #duplicates for check
    sequences_fasta_dup = []
    #sort sequences
    sorted_fasta = [f for f in sorted(sequences, key=lambda x : x.id)]
    sorted_names = []
    #take sequence names and count duplicates
    for s in sorted_fasta:
        name_split = s.name.split('/')
        name = name_split[0]
        sorted_names.append(name)
    name_dups = [item for item, count in collections.Counter(sorted_names).items() if count > 1]  
    #SKIP WHAT IS TO SKIP
    for name_to_skip in name_dups:
        if name_to_skip in which_sequence_to_skip:
            name_dups.remove(name_to_skip)
    #GET SEQUENCE NAMES
    for s in sequences:
        name_split = s.name.split('/')
        name = name_split[0]
        #SEPARATE DUPLICATES
        #print(temp_sequence_countainer)
        if name not in name_dups:
            sequence = str('>' + s.description + '\n' + s.seq + '\n')
            sequences_fasta.append(sequence)
        else:
            
            sequences_fasta_dup.append(s)
    #OUR ALL DUPLICATES IDS
    ids = []
        
    for s in sequences_fasta_dup:
        ids.append(s.name)        
    #GROUP DUPLICATES
    groups = [
      list(value) for key, value in 
      groupby(
        ids, 
        key=lambda element: element.split('/')[0]
      )
    ]
    print(groups)
    new_sequences = []
    c = 0
    #GET MIN/MAX FOR FIXED SEQENCE PER GROUP
    for group in groups:
        
        min_ = []
        max_ = []
        for element in group:
            element_parts = element.split('/')
            element_number = element_parts[1].split('-')
            min_.append(int(element_number[0]))
            max_.append(int(element_number[1]))
        from_ = min(min_)
        to_ = max(max_)
        id_parts = element_parts[0].split('_')
        id_ = id_parts[0]
        
############################################################################
###############SEQUENCE DOWNLOAD############################################
############################################################################
        try:              
            base_url = 'http://www.uniprot.org/uniprot/'
            current_url = base_url + id_ + '.fasta'
            response = r.post(current_url)
            cData = ''.join(response.text)
            c += 1
            print(c)
            Seq = StringIO(cData)
            pSeq = list(SeqIO.parse(Seq,'fasta'))
            new_sequence = str('>' + pSeq[0].name + '/' + str(from_) + '-' + str(to_) + '\n' + pSeq[0].seq[from_-1:to_] + '\n')
            new_sequences.append(new_sequence)
        except:
            print('sequence obsolete!: ', element_parts[0])
#            obsolete = str('>' + id_ + '/' + str(from_) + '-' + str(to_) + '\n')
#            new_sequences.append(obsolete)
            continue
    result_fasta = sequences_fasta + new_sequences
    with open(result_name_maker(filename),'w') as w:
        for s in result_fasta:
            w.write(s)
