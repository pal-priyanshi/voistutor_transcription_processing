#!/usr/bin/env python
# coding: utf-8

# In[24]:


def part4(file1,file2):
    import re
    import io
    if ".txt" in file1:
        with open(file1,'r', encoding="utf-8") as f:
            contents = f.read()
    else:
        contents=file1
    if ".txt" in file2:
        with open(file2,'r', encoding="utf-8") as f:
            invalids = f.read()
    else:
        invalids=file2
    with open('forPhoneMapping.txt','r', encoding="utf-8") as f:
        phone_content_f = f.read()
    with open('timitIPAtoArpa.txt','r', encoding="utf-8") as f2:
        timit_content_f = f2.read()
        
    with open(file2,'r', encoding="utf-8") as f:
        invalids = f.read()
    phone_map={}
    timit_map={}
    phonemap=re.findall(r'(\S+)\t.*\t(.*)', phone_content_f)
    for i,y in phonemap:
        phone_map[i]=y
    timitmap=re.findall(r'(\S+)\t(\S+)', timit_content_f)
    for j,k in timitmap:
        timit_map[j]=k
    print(len(phone_map), len(timit_map))
    contents=re.sub(r' +:',':',contents)
    contents=re.sub(r' ̪+','̪',contents)
    contents=re.sub(r' ?~ ?', ' ~ ',contents)  #making spacing consistent around ~
    contents=re.sub(r' +',' ', contents) #replacing consecutive spaces to single space
    contents=re.sub(u'[\xc2\xa0\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u2028\u2029\u202F\u205F\u3000]',' ', contents) #replacing non breaking spaces with space
    pattern3=re.findall(r'(.*)(file_\d\d\d\d.wav) (.*)\b(?:\?,|\?\.,|!\.,|\.,|\.\.,|\)\.,)(.*)(?:\?|\!|\.|\))*\n?', contents) #(\?|\!|\.|\))*
    print(len(pattern3))
    files=[]
    f_n_t={}
    ts_n_f={}
    f_n_t_corr={}
    invalid_sym=re.findall(r'file_\d+.wav (.*)\t(.*)', invalids) #file_number,invalid symbol,valid symbol in sequence per line
    print(len(invalid_sym)) #loading invalid,valid values
    correction_itv={}
    for x,y in invalid_sym:
        correction_itv[x]=y
    for x,y,z,p in pattern3: #x=ts, y=files, z=sentences,p=phonetic transcription
        p=re.sub(r'[\?\!\.,;\)\(]','',p)
        p=re.sub(r'(?<!~) +:',':',p)
        p=re.sub(r'\s+$','', p)
        p=re.sub(r'^\s+','', p)
        files.append(y)
        f_n_t[y]=p #file and transcription dictionary key=file, value=phonetic transcription
        ts_n_f[y]=x #time stamp and file number dictionary
        pat_=re.findall(r'[^\s~]+', p)
        for j in pat_: 
            if j in correction_itv:
                if re.search(r'^[^\s~]+',p).group(0)==j: #if a transcription starts with invalid phonetic symbol
                    p=re.sub(rf'(?<!\D){j}(?= )',correction_itv[j],p) #check if nothing is in front of it and is followed by a space
                if re.search(r'[^\s]+$',p).group(0)==j: #if invalid symbol is a the end of a transcription line
                    p=re.sub(rf'{j}',correction_itv[j],p) #replace it with corrected symbol (space may or may not be there before it)
                else:
                    p=re.sub(rf'(?<= ){j}(?= )',correction_itv[j],p) #else check for space before and after then only replace it
        p=re.sub(r'^ +','',p)
        p=re.sub(r' +$','',p)
        p=re.sub(r' +',' ',p)
        f_n_t_corr[y]=p
        #After correction, verify if there's any unexpected invalid symbol created.
        pat_2=re.findall(r'[^\s~]+', p)
        for j in pat_2:
            if j not in phone_map and j not in timit_map:
                print(j,y, "invalid found")
    saving_sorted_string=""
    for i in sorted(files):
        saving_sorted_string+=ts_n_f[i]+i+" "+f_n_t_corr[i]+"\n"
    #with io.open('corrected_Unique_del.txt', 'w', encoding='utf-8') as f:
     #   f.write(saving_sorted_string)
    return saving_sorted_string

#import io
#with io.open('corrected_combined_formatted_set_1_2.txt', 'w', encoding='utf-8') as f:
   # f.write(saving_sorted_string)


# In[23]:


p4out=part4("Unique_transcriptions_from_linguists_modv.txt","invalid_symbol_list_trans_from_linguists2v.txt")


# In[26]:


p4out=part4("Unique_combined_del.txt","invalid_symbol_list_shar_sid_vfinredo.txt")


# In[46]:


#file tracking
#Input task 1: Unique_transcriptions_from_linguists_modv.txt, invalid_symbol_list_trans_from_linguists.txt
#Input task 2: Unique_combined_shar_sid_modv.txt, invalid_symbol_list_shar_sid_fn.txt
#Input task 3: combined_formatted_set_1_2.txt, invalid_symbol_list_converted_set_1_2_mod.txt


# In[ ]:


#Output file, task 1: corrected_Unique_trans_from_linguist.txt
#Output file, task 2: corrected_Unique_combined_shar_sid.txt
#Output file, task 3: corrected_combined_formatted_set_1_2.txt


# In[208]:


#print(re.findall(r'\xa0|\xc2|\xc2\xa0|\xa0\xc2',contents))

