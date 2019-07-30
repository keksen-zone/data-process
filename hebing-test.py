import os
filedir = os.getcwd()+'\\input_files'
#filenames=os.listdir(filedir)
filenames=['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt','file5.txt', 'file6.txt', 'file7.txt', 'file8.txt', 'file9.txt','file10.txt']
print(filenames)
file=open('output','w')
for f_n in filenames:
    filepath=filedir+'\\'+f_n
    for line in open(filepath):
        file.writelines(line)
        print(line,end='')
    file.write('\n')
file.close()