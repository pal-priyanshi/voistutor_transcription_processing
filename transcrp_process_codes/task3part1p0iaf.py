#!/usr/bin/env python
# coding: utf-8

# In[8]:
import re
import docx2txt
import glob
import os

def t3part1p0(x):
    from timeit import default_timer as timer
    start=timer()
    try:
        with open(x,'r', encoding="utf-8") as f:
            part=f.read()
    except:
        part=x
    f1=""
    #print("count of file no's in passed paramter=", len(re.findall(r'file_\d+.wav',part)))
    with open("transcription wordfile1619-1719.txt",'r', encoding="utf-8") as f:
        f1 = f1+f.read()
    for file_name in glob.iglob('C:\\Users\\priya\\Documents\\work\\prasanta\\work\\task 2\\CORRECTED SET 1 & 2-20200807T113500Z-001\\CORRECTED SET 1 _ 2/*.docx', recursive=True):
        #print(os.path.basename(file_name))
        f1=f1+docx2txt.process(os.path.basename(file_name))+"\n"
    print(len(re.findall(r'file_\d+.wav', f1)), len(set(re.findall(r'file_\d+.wav', f1)))) #checking if all files are unique.
    f1=re.sub(r' +$','', f1, flags=re.MULTILINE) #replacing lines ending with spaces and new line with just a new line
    formatted=""
    pattern=re.findall(r'\t?,?(file_\d\d\d\d.wav)\t?\n*(.*)\n+\t? *(.*)\n+', f1)
    for x,y,z in pattern:
        formatted+=x+" "+y+".,"+z+"\n"
    combined=part+formatted
    pattern3=re.findall(r'(file_\d\d\d\d.wav) (.*)\b(\?,|\?\.,|!\.,|\.,|\.\.,|\)\.,){1}(.*)(\?|\!|\.|\))*\n', combined)
    print("length of lines fitting pattern in combined" ,len(pattern3))
    print("number of file no's in combined=",len(re.findall(r'file_\d+.wav', combined))) #should match with above pattern length.
    end=timer()
    print("--- %s seconds for task3part1 glob one---", end-start)

    return combined
    

# In[16]:


#import io
#with io.open('combined_formatted_set_1_2.txt', 'w', encoding='utf-8') as f: #had an empty text file with this name in a directory already created
#    f.write(combined)


# In[9]:


#z=t3part1p0("Unique_sharmistha-output-formatted.txt")


# In[ ]:




