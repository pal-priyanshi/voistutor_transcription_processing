#!/usr/bin/env python
# coding: utf-8

# In[38]:
import re
import io

def part1(file):
    from timeit import default_timer as timer
    start=timer()
    try:
        with open(file,'r', encoding="utf-8") as f:
            contents = f.read()
    except:
        contents=file
    time_stamps=[]  #Block Function: To extract time stamps, file number, english sentences and phonetic transcription from lines in text file
    eve=[]
    check_phone=[]
    file_name=[]
    pattern_test2=re.compile(r',(\d\d/\d\d/[0-9]{4} \d\d:\d\d:\d\d),(file_\d\d\d\d\.wav),(.*)\n?', re.MULTILINE)#'\b(\?,|\?\.,|!\.,|\.,|\.\.,|\)\.,){1}(.*)(\?|\!|\.)*\n?')
    matches_test2=pattern_test2.finditer(contents)
    filename_pat=re.compile(r'(file_\d\d\d\d\.wav)')
    filename_mat=filename_pat.findall(contents)
    for i in matches_test2: #extracting time stamps, file names and transcription(eng sentence+phoneme) by matching regex pattern
        time_stamps.append(i.group(1))
        file_name.append(i.group(2))
        eve.append(i.group(3))
    print(len(file_name), len((eve)), len(time_stamps), len(filename_mat), len(set(time_stamps)))
    print("unique file numbers=", len(set(file_name)))
    
    #Block function:If there's time stamp which is repeating, check if it has same/diff file number and transcription
    for i in set(time_stamps):
        if time_stamps.count(i)>1:
            compare_fn=file_name[time_stamps.index(i)]
            compare_eve=eve[time_stamps.index(i)]
            for x,y,z in zip(time_stamps, file_name, eve):
                if x==i:
                    if y!=compare_fn: 
                        print("same_ts, diff file name", y) #in this case, no two different files have same time stamp
                    #if z!=compare_eve: #same time stamps, same file, different transcription (almost same transcription except a minor difference)
                        #print("diff trans",y, compare_fn)
                        #print(compare_eve)
                        #print(z)
                        
    tsdigits=[] #Block Function: To reformat time format from d,m,y to y,m,d for comparison of a later time to earlier one
    ts_str=""
    for i in time_stamps:
        diff_p=re.compile(r'(\d\d)/(\d\d)/([0-9]{4}) (\d\d:\d\d:\d\d)')
        diff_m=diff_p.finditer(i)
        for i in diff_m:
            ts_str=(i.group(3))+(i.group(2))+(i.group(1))+(i.group(4)) #year, month, date, time
            ts_str=ts_str.replace(":","")
            tsdigits.append(int(ts_str))
            
    corresp=[] #Block Function: for files which are repeating, take last time stamp value index for those(stored in corresp)
    track=[]
    for i in set(file_name): 
        if file_name.count(i)>1:#if file is repeating in file names
            for j,x in enumerate(file_name):    
                if x==i: 
                    track.append(tsdigits[j])#get all time stamps value associated with that file and take the one with max/latest value            
            corresp.append(tsdigits.index(max(track))) #store index of latest time stamp in a list
            track.clear()                  
    print(len(corresp))
    
    fin_string=""
    total_files_count=0
    for k,j in enumerate(file_name):
        if file_name.count(j)==1: #using indices of files which occur only once
            fin_string+=time_stamps[k]+" "+j+" "+eve[k]+"\n"
            total_files_count+=1
        if k in corresp: #indices according to latest time stamps' index value for repeating files
            fin_string+=time_stamps[k]+" "+file_name[k]+" "+eve[k]+"\n"
            total_files_count+=1
    print((total_files_count))
    
    ##Verification
    counter=0
    matches=re.findall(r'(.*) (file_\d\d\d\d.wav) (.*)\n', fin_string) #checking in our processed string
    for x,y,z in matches:
        pat_un=re.findall(x+r','+y+r','+re.escape(z), contents) 
        if pat_un==[]: #if there are no matches, count the number of failed matches
            counter+=1
    print("number of unmatches=", counter) #should print 0 number of counts that it didn't match i.e all macthed in source file.
    #with io.open('Unique_transcriptions_from_linguists_modv2.txt', 'w', encoding='utf-8') as f: #had an empty text file with this name in a directory already created
     #   f.write(fin_string)
    end=timer()
    print("--- %s seconds task1part1 ---", end-start)
    return fin_string
##output
#with io.open('Unique_combined_shar_sid_modv.txt', 'w', encoding='utf-8') as f: #had an empty text file with this name in a directory already created
#    f.write(fin_string)


# In[39]:


#p1out= part1("transcription-from-linguists-Unique.txt")


# In[ ]:


#Input file, task 1: transcription-from-linguists-Unique.txt
#Input file, task 2: combined_shar_sid_modv.txt
#Input file, task 3: sharmistha-output-formatted.txt


# In[ ]:


#Output file, task 1: Unique_transcriptions_from_linguists_modv.txt
#Output file, task 2: Unique_combined_shar_sid_modv.txt
#Output file, task 3: Unique_sharmistha-output-formatted.txt

