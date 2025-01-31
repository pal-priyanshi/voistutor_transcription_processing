#!/usr/bin/env python
# coding: utf-8

# In[5]:
import re
import io

def inv2v(file1,file2):
    from timeit import default_timer as timer
    start=timer()
    try:
        with open(file1,'r', encoding="utf-8") as f: #(fixed file) #invalid_symbol_list_shar_sid_fn_old_nice.txt
            ap=f.read()
    except:
        ap=file1
    try:
        with open(file2,'r', encoding="utf-8") as f1: #file to fill up with valids
            np=f1.read()
    except:
        np=file2
    ap_inv=re.findall(r'file_\d+.wav (.*)\t.*\n',ap)
    ap_v=re.findall(r'file_\d+.wav .*\t(.*)\n',ap)
    ap_dict={}
    np_inv=re.findall(r'file_\d+.wav (.*)\t.*\n',np)
    np_filez=re.findall(r'(file_\d+.wav) .*\t.*\n',np)
    print(len(ap_inv),len(ap_v))
    for i,j in zip(ap_inv,ap_v):
        ap_dict[i]=j
    inv2vtxt=""
    counting=0
    for i,j in zip(np_filez, np_inv):
        if j in ap_dict:
            inv2vtxt+=i+" "+j+"\t"+ap_dict[j]+"\n"
            counting+=1
        else:
            inv2vtxt+=i+" "+j+"\t"+j+"\n"
            counting+=1
    print(counting)
    for i in np_inv:
        if i not in ap_inv:
            print(i,"not there")
    #with io.open('invalid_symbol_list_trans_from_linguists2valid.txt', 'w', encoding='utf-8') as f:
     #d   f.write(inv2vtxt)
    end=timer()
    print("--- %s seconds for inv2v ---",end-start)
    return inv2vtxt

        #inv2vtxt+=i+""


# In[6]:


#x=inv2v("invalid_symbol_list_transcription_from_linguists.txt","invalid_symbol_list_trans_from_linguists2.txt")


# In[ ]:




