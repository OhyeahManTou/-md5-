#-*- coding: utf-8 -*-
import hashlib   
import os
import io
import sys
import re

LUJING = raw_input('请输入路径：')

def geneMd5(filename):
    # 算md5
    m = hashlib.md5()
    file = io.FileIO(filename,'r')
    bytes = file.read(1024)
    while(bytes != b''):
        m.update(bytes)
        bytes = file.read(1024) 
    file.close()
    return m.hexdigest()

def md5_js():
    file_ = []
    file_md5 = []
    if(len(sys.argv)==1):
        path=LUJING
    if(len(sys.argv)==2):
        path=sys.argv[1]
    for fpathe,dirs,fs in os.walk(path):
        for f in fs:
            full_file = os.path.join(fpathe,f)
            file_.append(full_file)
            file_md5.append(geneMd5(full_file))
    Trunk_md5 = dict(zip(file_, file_md5))
    for k,v in Trunk_md5.items():
        print (k,v)

md5_js()
