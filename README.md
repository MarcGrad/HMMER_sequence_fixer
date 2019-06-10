# HMMER_sequence_fixer v3
this is still preliminary version
please msg me if want help me upgrade script!

restrictions: works only with uniprot id, only fasta format

This simple script can help fix phmmer, jackhmmer cut sequence domains or with Pfam unaligned fasta 
example: https://pfam.xfam.org/family/PF07804/alignment/rp15/format?format=fasta&alnType=rp15&order=t&case=u&gaps=none&download=0

how to use: 
1. enter filename
2. enter sequences you want to skip
3. run!

example:
>A0A0W0YFE9_9GAMM/12-101
IGPNPQKAHAATHMFTEGAFPGHSSNWIVKIADDPIIARHEVLAQELFRLFIPHQPQTRI
AKDEKDYFVCSEKVESYKSLPYGEGKRFED
>A0A0W0YFE9_9GAMM/88-219
YKSLPYGEGKRFEDGTYTGLGQAILVAVFLQEVDLKNGNIGLDKDNRVIKIDGDQCLASV
LEGRLHFALTPEVIATLPRKGDFAANNWLDDKSTSTSFSTSKILNHTTISKNELFRGEIN
QAMLKICLLPDE
   ;;;;;
   ;;;;;
   ;;;;;
   ;;;;;
 ..;;;;;..
  ':::::'
    ':`
>tr|A0A0W0YFE9|A0A0W0YFE9_9GAMM/12-219
IGPNPQKAHAATHMFTEGAFPGHSSNWIVKIADDPIIARHEVLAQELFRLFIPHQPQTRI
AKDEKDYFVCSEKVESYKSLPYGEGKRFEDGTYTGLGQAILVAVFLQEVDLKNGNIGLDK
DNRVIKIDGDQCLASVLEGRLHFALTPEVIATLPRKGDFAANNWLDDKSTSTSFSTSKIL
NHTTISKNELFRGEINQAMLKICLLPDE

If there is any domain duplicate you can skip sequences with duplicates, by giving sequence id in list 'which_sequence_to_skip' 
(soon it will be upgraded)

NEED python3

requirements (libaries):
requests (2.21.0)
Bio (1.73)
