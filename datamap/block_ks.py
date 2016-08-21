#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import os
import re

def read_block_rr_txt(fn):
    f1=open(fn)#block.rr.txt
    data=[]
    b=[]
    flag=0
    for line in f1.readlines():
        line=line.strip()
        #print(line)
        if re.match(r"the",line):
            b=[]
            flag=1
            continue
        if flag==0:
            continue
        if re.match(r"\>",line):
            flag=0
            if len(b)==0:
                continue
            #print(b)
            #c=[k[2] for k in b]
            p=re.findall(r"\d+\.\d+",line)
            data.append([b,p[0]])
            b=[]            
            #print(c)
        a=re.split(r"\s",line)
        #print(a[2])
        b.append([a[0],a[2]])
    f1.close()
    return data

def read_ks_txt(fn):
    f=open(fn)#block.rr.ks.txt
    dict={}
    for line in f.readlines():
        line=line.strip()
        arr=re.split(r"\t",line)
        #print(len(arr))
        dict[str(arr[0])+"\t"+str(arr[1])]=arr[3]
        dict[str(arr[1])+"\t"+str(arr[0])]=arr[3]
        #print(str(arr[0])+"\t"+str(arr[1]))
    f.close()
    return dict

def block_ks(data,dict):
    array=[]
    for i in range(len(data)):
        a=[]
        for k in  data[i][0]:
            if(str(k[0])+"\t"+str(k[1]) not in dict.keys()):
                print(str(k[0])+"\t"+str(k[1]))
                continue
            b=float(dict[str(k[0])+"\t"+str(k[1])])
            #print(str(k[0])+"\t"+str(k[1]))
            if(b <0 or b>1.8):
                #print(b)
                continue
            a.append(float(b))
        if(float(len(a)/len(data[i][0]))<=0.25):
            print(float(len(a)/len(data[i][0])))
            continue
        if(len(a)>2 and float(data[i][1])<=0.05):
            array.append([float(sum(a)/len(a)),str(data[i][1]),len(a)])
            #array.append([float(a[int(len(a)/2)]),str(data[i][1]),len(a)])
        #print(sum(a),float(sum(a)/len(a)),len(a))
    return array		
	
if __name__=="__main__":
    data=read_block_rr_txt(sys.argv[1])
    dict=read_ks_txt(sys.argv[2]) 
    #print(len(data))
    res=block_ks(data,dict)
    print(len([float(k[0]) for k in res]))
    f=open(sys.argv[3],'w+')
    for k in res:
        f.write(str(k[0])+"\t"+str(k[1])+"\t"+str(k[2])+"\n")
    #print(res)	
  	