#!/usr/bin/env python
#coding:utf-8 

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
from Bio import SeqIO
import re
import sys

def read_cds_fa(fn):
	gc=[]
	for seq_record in SeqIO.parse(fn, "fasta"):
		gc.append([seq_record.id,GC(seq_record.seq)])
	return gc 

if __name__ == "__main__":
    gc=read_cds_fa(sys.argv[1])
    f=open(sys.argv[2],'w+')
    for k in gc:
    	f.write(str(k[0])+"\t"+str(k[1])+"\n")