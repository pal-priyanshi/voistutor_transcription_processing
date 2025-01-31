#!/usr/bin/env python
# coding: utf-8

# In[1]:
import re
import io

def part6(file,file2):
    with open('myphones.64-48-40.map','r', encoding="utf-8") as f:
        myphones = f.read()
    try:
        with open(file,'r', encoding="utf-8") as f:
            contents = f.read()
    except:
        contents=file
    with open(file2,'r', encoding="utf-8") as f: #'subMapInfo_3034.txt'
        submapinfo = f.read()
    submapdict={}
    submap=re.findall(r'(\w+ *\w+_.*) \t?(file_\d+\.wav)',submapinfo)
    for a,b in submap:
        a=re.sub(r' +','_',a)
        submapdict[b]=a
    mp_dict={}
    mp_pat=re.findall(r'(\S+)\t*\S*\t*(\S+)*\n?',myphones) 
    #mp_matches=mp_pat.finditer(myphones)
    for i,j in mp_pat:
        mp_dict[i]=j #myphones.64-48-40 dictionary
    #print(len(mp_dict))
    line_pattern=re.findall(r'(file_\d+.wav) (.*)', contents, re.MULTILINE)
    converted_string=""
    converted_string_wfn=""
    #converted_string_wfn2=""
    for k,(z,i) in enumerate(line_pattern):
        tempy=i
        mat_fin=re.findall(r'[^\s\d_~]{3,}',i)#(r'[^~]?\S+[^~]?')
        mat_fin2=re.findall(r'[^\s\d_~]{2}',i)
        mat_fin3=re.findall(r'[^\s\d_~]',i)
        for j in mat_fin:
                #print(j)
            if j in mp_dict:
                i=i.replace(j,mp_dict[j])
        for j in mat_fin2:
            if j in mp_dict:
                i=i.replace(j,mp_dict[j])
        for j in mat_fin3:
            if j in mp_dict:
                i=i.replace(j,mp_dict[j])
        converted_string+=submapdict[z]+" "+i+"\n"
        ##VERIFICATION
        check_pat=re.findall(r'[^\s~]+',i)
        for j in check_pat:
            if j not in mp_dict.values():
                print(j,"unconverted")
    #with io.open('processed_trans_from_linguists_latest.txt', 'w', encoding='utf-8') as f:
     #    f.write(converted_string)
    converted_string=re.sub(r' +',' ', converted_string)
    return converted_string


# In[2]:


#p6out=part6("IPAtoARPA_shar_sid.txt")


# In[2]:


#p6out=part6("IPAtoArpa_converted_set_1_2.txt","subMapInfo.txt")


# In[51]:


#import io
#with io.open('aaaaaaaa.txt', 'w', encoding='utf-8') as f:
 #   f.write(p6out)


# In[ ]:


#Input file, task 1: IPAtoARPA_trans_from_linguists.txt
#Input file, task 2: IPAtoArpa_shar_sid.txt
#Input file, task 3: IPAtoArpa_converted_set_1_2.txt


# In[ ]:


#Output file, task 1: processed_trans_from_linguists.txt
#Output file, task 2: processed_shar_sid.txt
#Output file, task 3: processed_converted_set_1_2.txt


# In[ ]:




