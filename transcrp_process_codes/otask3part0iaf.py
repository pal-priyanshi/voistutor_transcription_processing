#!/usr/bin/env python
# coding: utf-8

# In[2]:

import re
import io
def t3part0():
    from timeit import default_timer as timer
    start=timer()
    with open('sharmistha-output.txt','r', encoding="utf-8") as f:
        content_1 = f.read()
    content_1=re.sub(r'\n+','\n', content_1) 
    content_1=re.sub(r' *\n(?=,\D+)','.',content_1)
    file_pat=re.findall(r'file_\d\d\d\d.wav', content_1)
    print(len(file_pat))

    pattern3=re.findall(r'(file_\d\d\d\d.wav),(.*)\b(\?,|\?\.,|!\.,|\.,|\.\.,|\)\.,){1}(.*)(?:\?|\!|\.|\))*\n?', content_1)
    print(len(pattern3))
    ##Verification
    for a,b,c,d in pattern3: #double checking if all delimiters are expected
        #if c=='':
        if c not in ['?,','?.,','!.,','.,','..,',').,']:
            print(c)
    count=0 
    for i in content_1.splitlines():
        count+=1
    print(count) #should be equal to len(file_pat)
    end=timer()
    print("--- %s seconds for t3part0---" , (end - start))
    return content_1
#with io.open('sharmistha-output-formatted.txt', 'w', encoding='utf-8') as f: #had an empty text file with this name in a directory already created
 #   f.write(content_1)


# In[3]:


#zz=t3part0()
#print(zz)


# In[ ]:




