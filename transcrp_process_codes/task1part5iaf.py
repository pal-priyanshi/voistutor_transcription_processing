#!/usr/bin/env python
# coding: utf-8

# In[34]:

import re
import io
def part5(file): 
    try:
        with open(file,'r', encoding="utf-8") as f:
            contents = f.read()
    except:
        contents=file
    with open('forPhoneMapping.txt','r', encoding="utf-8") as f:
        phone_content_f = f.read()
    with open('timitIPAtoArpa.txt','r', encoding="utf-8") as f2:
        timit_content_f = f2.read()
    phone_map_count=0
    total_dict={}
    timit_map_count=0
    phonemap=re.findall(r'(\S+)\t.*\t(.*)', phone_content_f)
    for i,y in phonemap:
        total_dict[i]=y
        phone_map_count+=1
    timitmap=re.findall(r'(\S+)\t(\S+)', timit_content_f)
    for j,k in timitmap:
        total_dict[j]=k.upper()
        timit_map_count+=1
    print("phonemes in forPhoneMaping=",(phone_map_count), ", phonemes in timitIPAtoArpa=",(timit_map_count), ", total unique symbols in both=",len(total_dict))
    pattern=re.findall(r'.*(file_\d\d\d\d.wav) (.*)\n', contents) #(\?|\!|\.|\))*
    converted_str=""
    invalid_chars=[]
    for x,p in pattern:
        mat_=re.findall(r'[^\s~]{3,}',p)
        mat1_=re.findall(r'[^\s~]{2}',p)#(r'\S{2,3}') #match symbols with two or 3 characters like i: / t̪ / d̪h (counted as char length=3)
        mat2_=re.findall(r'[^\s~]',p)#(r'\S{1}') #match single character like ɽ or ɖ etc
        for j in mat_: #matches for len(char)=3
            if j in total_dict:
                p=p.replace(j, total_dict[j])
        for m in mat1_: ##matches for len(char)=2
            if m in total_dict:
                p=p.replace(m, total_dict[m])
        for l in mat2_: #matches for len(char)=1
            if l in total_dict:
                p=p.replace(l, total_dict[l])
            #print(i)
        p=re.sub(r' +',' ',p)
        p=re.sub(r'\t+',' ',p)
        #verification-1 :to ensure if all got converted, checking if any phonetic symbol doesn't match the arpa symbols (dictionary values) 
        check_pat=re.findall(r'[^\s~]+',p)
        invalid_chars.append([t for t in check_pat if t not in total_dict.values()]) 
        #verification-2 :If anything is left unconverted, it will appear in lower case
        for j in check_pat:
            if j.islower()==True:
                print(i,"unconverted")
        converted_str+=x+" "+p.lower()+"\n" #processed string from IPA to ARPA
    print("number of arpa symbols not in forPhoneMapping or timitIPAtoArpa=",len(list(filter(None, invalid_chars)))) #len should be 0- output of verification method 1
   # with io.open('IPAtoARPA_trans_from_linguists_latest.txt', 'w', encoding='utf-8') as f:
    #    f.write(converted_str)
    return converted_str


# In[6]:


#pout5=part5("corrected_Unique_combined_shar_sid.txt")


# In[35]:


#pout5=part5("corrected_Unique_trans_from_linguist_latest.txt")


# In[4]:


#Input file, task 1: corrected_Unique_trans_from_linguist.txt
#Input file, task 2: corrected_Unique_combined_shar_sid.txt
#Input file, task 3: corrected_combined_formatted_set_1_2.txt


# In[11]:


#for i in f_n_t_col.values():
 #   check_pat=re.findall(r'[^\s~]',i)
  #  for j in check_pat:
   #     if j.islower()==True:
    #        print(i)


# In[ ]:


#Output file, task 1: IPAtoARPA_trans_from_linguists.txt
#Output file, task 2: IPAtoArpa_shar_sid.txt
#Output file, task 3: IPAtoArpa_converted_set_1_2.txt


# In[ ]:




