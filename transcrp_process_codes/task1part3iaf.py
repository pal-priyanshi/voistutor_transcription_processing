#!/usr/bin/env python
# coding: utf-8

# In[8]:
import re
import io

def part3(file):
    from timeit import default_timer as timer
    start=timer()
    with open('forPhoneMapping.txt','r', encoding="utf-8") as f:
        phone_content_f = f.read()
    with open('timitIPAtoArpa.txt','r', encoding="utf-8") as f2:
        timit_content_f = f2.read()
    try:
        with open(file,'r', encoding="utf-8") as f:
            ups = f.read()
    except:
        ups=file
    phone_col1=re.findall(r'(\S+)\t.*\t.*', phone_content_f)
    timit_col1=re.findall(r'(\S+)\t\S+', timit_content_f)
    #print(len(set(phone_col1)), len(set(timit_col1)))
    f_n_s=re.findall(r'(file_\d\d\d\d.wav) (.*)\n', ups)
    total_valid=[]
    for i in phone_col1:
        total_valid.append(i)
    for i in timit_col1:
        total_valid.append(i)
    print("total valid symbols in forPhoneMapping and timitIPAtoArpa=",len(total_valid), ", total unique valid symbols=", len(set(total_valid)))
    unique_invalid_sym=""
    nfunique_invalid_sym=""
    valids=[]
    valids1=[]
    invalids=[]
    invalids2=[]
    for p,q in f_n_s :
        if q in set(total_valid):
            valids1.append(q)
        else:
            invalids2.append(q)
        if q not in timit_col1 and q not in phone_col1:
            invalids.append(q)
            unique_invalid_sym+=p+" "+q+"\t"+q+"\n" 
            nfunique_invalid_sym+=q+"\t"+q+"\n"
        else:
            valids.append(q)
    print("valid, invalid count method 1=", len(valids), len(invalids), ", valid invalid count method 2=",len(valids1), len(invalids2))
    #with io.open('invalid_symbol_list_trans_from_linguists2.txt', 'w', encoding='utf-8') as f:
     #   f.write(unique_invalid_sym)
    #with io.open('C_invalid_symbol_list_converted_set_1_2.txt', 'w', encoding='utf-8') as f:
 #   f.write(unique_invalid_sym)
    end = timer()
    print("--- %s seconds for task1part3---", end-start)
    return unique_invalid_sym


# In[4]:


#p3out=part3("unique_phoneme_symbols_trans_from_linguists2.txt")


# In[9]:


#p3out=part3("unique_phoneme_symbols_trans_from_linguists2.txt")


# In[46]:


#FILE TRACKING:
# Input for TASK 1: unique_phoneme_symbols_trans_from_linguists.txt
# Input for TASK 2: unique_phoneme_symbols_shar_sid.txt
# Input for Task 3: unique_phoneme_symbols_converted_set_1_2.txt


# In[ ]:





# In[43]:


#Output file, Task 1: invalid_symbol_list_trans_from_linguists.txt
#Output file, Task 2: invalid_symbol_list_shar_sid_fn.txt
#Output file, Task 3: invalid_symbol_list_converted_set_1_2.txt


# In[ ]:




