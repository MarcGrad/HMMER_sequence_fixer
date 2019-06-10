# HMMER_sequence_fixer v3 
This is still preliminary version :octocat:

please msg me if want help me upgrade script!

restrictions: works only with uniprot id, only fasta format

This simple script can help fix  :construction_worker: phmmer, jackhmmer cut up  :scissors: sequences domains or with Pfam unaligned fasta 
example: https://pfam.xfam.org/family/PF07804/alignment/rp15/format?format=fasta&alnType=rp15&order=t&case=u&gaps=none&download=0

how to use: 
1. enter filename
2. enter sequences you want to skip
3. run! :running:

If there is any domain duplicate you can skip this sequences, by giving sequence id in list 'which_sequence_to_skip' 
(soon it will be upgraded)

NEED python3 :snake:

requirements (libaries):

requests (2.21.0)

Bio (1.73)
