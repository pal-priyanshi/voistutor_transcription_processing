#!/usr/bin/env python
# coding: utf-8

# In[4]:
import re
import io

def part2n(file):
    from timeit import default_timer as timer
    start=timer()
    try:
        with open(file,'r', encoding="utf-8") as f:
            utfl = f.read()
    except:
        utfl=file
    with open('approximate_mapping.txt','r', encoding="utf-8") as f:
        approx_mapping = f.read()
    approx_map=re.findall(r'(.*)\t(.*)',approx_mapping)
    for a,b in approx_map:
        utfl=utfl.replace(a,b)
    utfl=re.sub(u'[\xc2\xa0\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u2028\u2029\u202F\u205F\u3000]',' ', utfl) #replacing non breaking spaces with space
    f_n_t={}
    sentences=[]
    pattern3=re.findall(r'.*(file_\d\d\d\d.wav) (.*)\b(\?,|\?\.,|!\.,|\.,|\.\.,|\)\.,){1}(.*)(\?|\!|\.|\))*\n', utfl)
    print("count of lines fitting pattern p2=", len(pattern3))
    for x,y,z,p,q in pattern3:
        p=re.sub(r'[\?\!\.,;]','',p)
        p=re.sub(r' +:',':',p)
        p=re.sub(r' ̪+','̪',p)
        f_n_t[x]=p 
        sentences.append(y)
    print("total instances of file+transcription=",len(f_n_t)) #file-transcription mapping, key=file, value=transcription
    single_str=""
    problematic=""
    counting=0
    counting2=0
    pat=re.compile(r'[^\s\)\(\?\!,;\.~]+', re.MULTILINE)
    #pat=re.compile(u'[\u0250-\u02AF]+', re.UNICODE)
    #pat=re.compile(u'[^\W\d]+', re.UNICODE)
    idict_c={}
    total_symbols=[]
    z=0
    for p,q in f_n_t.items(): #p= file number, q=phonetic transcription
        #if "\t" in q:
         #   print(p,q)
        single_str+=q+"\n"
        mat=pat.findall(q)
        #print(q)
        for j in mat:
            idict_c[j]=p
            total_symbols.append(j)
    print("total phoneme symbols in the file=",len(total_symbols))
    total_sym_str=""
    for x,y in idict_c.items(): #iterating over phoneme symbol+file name pairs
        total_sym_str+=y+" "+x+"\n"
    #Verification code for checking if total phoneme symbols contain all characters in the document
    #pattern=re.compile(r'[^\s~]', re.MULTILINE)
    total_sum_count=0
    count_len=0
    for i in total_symbols:
        count_len+=len(i)
        #print(i, count_len)
    print("length of all phoneme symbols in txt file=",count_len) #length of all characters in total symbols
    single_str=re.sub(r'\?*\!*,*;*\)*\(*', '', single_str) #removing punctuations
    single_str=single_str.replace('.','') #removing .
    total_sum_count=len(single_str)-len(re.findall(r'[ \n\xc2\xa0\t~]', single_str))
    print("length of all symbols in txt file using verification method=",total_sum_count)
    #with io.open('unique_phoneme_symbols_trans_from_linguists2.txt', 'w', encoding='utf-8') as f: #had an empty text file with this name in a directory already created
     #   f.write(total_sym_str)
    end=timer()
    print("--- %s seconds for partp2n ---",end-start)
    return total_sym_str,utfl


# In[5]:


#y,z=part2n("combined_formatted_set_1_2.txt")


# In[14]:


#x=part2n("Unique_transcriptions_from_linguists_modv2.txt")


# In[2]:


#Input file, task 1: Unique_transcriptions_from_linguists_modv.txt
#Input file, task 2: Unique_combined_shar_sid_modv.txt
#Input file, task 3: combined_formatted_set_1_2.txt


# In[9]:


#Output file, task 1: unique_phoneme_symbols_trans_from_linguists.txt
#Output file, task 2: unique_phoneme_symbols_shar_sid.txt
#Output file, task 3: unique_phoneme_symbols_converted_set_1_2.txt


# In[10]:


#import io
#with io.open('unique_phoneme_symbols_converted_set_1_2.txt', 'w', encoding='utf-8') as f: #had an empty text file with this name in a directory already created
 #   f.write(total_sym_str)


# In[ ]:


#haven't come yet but for future: re.findall(r'[ \n\xc2\xa0\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u2028\u2029\u202F\u205F\u3000\t~]', single_str)

