#!/usr/bin/env python
# coding: utf-8

# In[6]:
import re
import io

def t2part0(file1,file2): #ex:file1= has to be sharmistha, file2=siddhartha
    with open(file1,'r', encoding="utf-8") as f:
        content_1 = f.read()
    with open(file2,'r', encoding="utf-8") as f1:
        content_2 = f1.read()
    content_1=re.sub(r'\n+','\n', content_1)
    content_2=re.sub(r'\n+','\n', content_2) #replacing multiple consecutive \n to single \n
    content_2=re.sub(r'\n+ +\n+','\n', content_2) #replacing \n space \n with just \n
    #bc2=content_2
    content_1=re.sub(r'\n *(?=[^\d\n,]+)', '', content_1)
    content_2=re.sub(r'\n *(?=[^\d\n,]+)', '',content_2)
    content_1=re.sub(r'\n(?=,\D+)','.',content_1) #merge phonetic transcription that starts in the next line to single line as rest of the transcription with the delimiter . so it becomes ., or ..,
    content_2=re.sub(r'\n(?=,\D+)','.',content_2) 
    content_1=re.sub(r'\!,', '!.,', content_1) #for lines where phonetic transcription end with ! and after conversion through last line becomes !, we change it to !., to fit it to our list of delimiters
    bc3=content_1+content_2
    transcription=re.findall(r',\d+.*,file_\d+.wav,(.*)',bc3)
    print(len(transcription)) #should match count mentioned below.
    count=0
    for i in bc3.splitlines():
        count+=1 #to check number of lines. This should match with the number found through the pattern search used later.
    print("total lines=",count)
    for i in transcription:
        temp=re.search(r'(.*)\b(\?,|\?\.,|!\.,|\.,|\.\.,|\)\.,)(.*)(\?|\!|\.|\))*',i)
        #print(type(temp))
        if temp==None: #all the lines where delimiter is a comma, potentially followed by space(', 'or ',')
            #print(i)
            if re.search(r',(?!\s)(.*)',i)!=None:
                x=i
                i=re.sub(r',(?!\s)','.,',i)
            if re.search(r'(?<!\s\w),(?!\w+) (.*)',i)!=None:
                x=i 
                i=re.sub(r'(?<!\s\w),(?!\w+) ','.,', i)
            bc3=bc3.replace(x,i)
    pattern3=re.findall(r'(file_\d\d\d\d.wav),(.*)\b(\?,|\?\.,|!\.,|\.,|\.\.,|\)\.,){1}(.*)(\?|\!|\.|\))*\n?', bc3)
    print("count of lines fitting pattern after changes=",len(pattern3)) #this should match count. 
    #with io.open('combined_shar_sid_deletedislater.txt', 'w', encoding='utf-8') as f: #had an empty text file with this name in a directory already created
     #   f.write(bc3)
    return bc3




