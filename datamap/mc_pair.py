#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import os
import re

def read_mc_txt(fn):
    f1=open(fn)
    dict={}
    for line in f1.readlines():
        line=line.strip()
        a=re.split(r"\t",line)
        #print(a)
        for i in range(1,len(a)):
            #print(a)
            if re.findall(r"[a-zA-Z]+",a[i]):
                 dict[str(a[0])+"\t"+str(a[1])]=1
    f1.close() 
    return dict

def read_block_rr_txt(fn):
    f1=open(fn)#block.rr.txt
    data=[]
    b=[]
    flag=0
    for line in f1.readlines():
        line=line.strip()
        #print(line)
        if re.match(r"^the",line):
            b=[]
            flag=1
            continue
        if flag==0:
            continue
        if re.match(r"\>",line):
            flag=0
            if len(b)==0:
                continue
            #print(len(b),b[0])
            #c=[k[2] for k in b]
            p=re.findall(r"\d+\.\d+",line)
            data.append([b,p[0]])
            b=[]            
            #print(c)
        a=re.split(r"\s+",line)
        #print(a[2])
        b.append(a)
    f1.close()
    return data

def block_choose(data,dict):
    res=[]
    for k in data:
        #print(k[0])
        b=[1 for a in k[0] if str(a[0])+"\t"+str(a[2]) in dict.keys()]
        #print(len(b))
        if len(b)>0:
            res.append(k)
    return res

if __name__=="__main__":
    data=read_block_rr_txt(sys.argv[2])
    dict=read_mc_txt(sys.argv[1]) 
    print(len(data))
    print(len(dict.keys()))
    res=block_choose(data,dict)
    f=open(sys.argv[3],'w+')
    print(len(res))
    for i in range(len(res)):
        f.write("the "+str(i)+"th path length "+str(len(res[i][0]))+"\n")
        for j in range(len(res[i][0])):
            for k in range(len(res[i][0][j])-1):
                f.write(str(res[i][0][j][k])+"\t")
            f.write(str(res[i][0][j][len(res[i][0][j])-1])+"\n")
        f.write(">LOCALE p-value : "+str(res[i][1])+"\n"+"\n")
    #print(res)	