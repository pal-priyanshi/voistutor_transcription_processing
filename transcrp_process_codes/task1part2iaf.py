#!/usr/bin/env python
# coding: utf-8

# In[52]:


def part2(file):    
    import re
    import io
    utfl=""
    if ".txt" in file and len(file)>100:
        with open(file,'r', encoding="utf-8") as f:
            utfl = f.read()
    else:
        utfl=file
    with open('approximate_mapping.txt','r', encoding="utf-8") as f:
        approx_mapping = f.read()
    approx_map=re.findall(r'(.*)\t(.*)',approx_mapping)
    for a,b in approx_map:
        utfl=utfl.replace(a,b)
    utfl=re.sub(u'[\xc2\xa0\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u2028\u2029\u202F\u205F\u3000]',' ', utfl) #replacing non breaking spaces with space
    f_n_t={}
    pattern3=re.findall(r'.*(file_\d\d\d\d.wav) .*\b(?:\?,|\?\.,|!\.,|\.,|\.\.,|\)\.,){1}(.*)(?:\?|\!|\.|\))*\n', utfl)
    single_str=""
    idict_c={}
    total_symbols=[]
    count_len=0
    t=[]
    total_sym_str=""
    for x,p in pattern3:#y,z,q #files, 
        p=re.sub(r'[\?\!\.,;]','',p) #remove punctuation
        p=re.sub(r' +:',':',p) # replace " :" with ":" so there's no space in examples like i:
        p=re.sub(r' ̪+','̪',p) 
        f_n_t[x]=p #
        single_str+=p+"\n"
        mat=re.findall(r'[^\s\)\(\?\!,;\.~]+',p)
        #print(q)
        for j in mat:
            idict_c[j]=x
            total_symbols.append(j)
            count_len+=len(j)
            if j not in t:
                t.append(j)
                total_sym_str+=idict_c[j]+" "+j+"\n"
    print(len(total_symbols))
    print(count_len) #length of all characters in total symbols
    single_str=re.sub(r'\?*\!*,*;*\)*\(*', '', single_str) #removing punctuations
    single_str=single_str.replace('.','') #removing .
    #Verification code for checking if total phoneme symbols contain all characters in the document
    total_sum_count=len(single_str)-len(re.findall(r'[ \n\xc2\xa0\t~]', single_str))
    print(total_sum_count)
    #with io.open('unique_phoneme_symbols_trans_from_linguists2.txt', 'w', encoding='utf-8') as f: #had an empty text file with this name in a directory already created
     #   f.write(total_sym_str)
    return total_sym_str,utfl


# In[5]:


#p2out=part2("Unique_transcriptions_from_linguists_modv.txt")


# In[53]:


#p2out=part2("combined_formatted_set_1_2.txt")


# In[50]:


#Input file, task 1: Unique_transcriptions_from_linguists_modv.txt
#Input file, task 2: Unique_combined_shar_sid_modv.txt
#Input file, task 3: combined_formatted_set_1_2.txt


# In[ ]:


#Output file, task 1: unique_phoneme_symbols_trans_from_linguists.txt
#Output file, task 2: unique_phoneme_symbols_shar_sid.txt
#Output file, task 3: unique_phoneme_symbols_converted_set_1_2.txt


# In[ ]:


#haven't come yet but for future: re.findall(r'[ \n\xc2\xa0\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u2028\u2029\u202F\u205F\u3000\t~]', single_str)

