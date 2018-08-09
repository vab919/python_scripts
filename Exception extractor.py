import re
import os
import mmap

#added comment to check update in github
os.chdir("C:\\py\\")

# get the directory where the logs are located

#print('The current directory is')
#print(os.getcwd())

# listing directories and files
#for f in os.listdir():
 #  file_name,file_ext =os.path.splitext(f)
  # print(file_name.split('a'))
#Method 1
# locate the relevant file

#f=open('j.log')
#lines=f.readlines()
#for line in lines:
#    if "error" in line:
#        print(line)
# extract specific part of the record
#   print(line.split()[3].split('.')[2])

# Search for the pattern

# extract the required information from the file

# output to desired location

#Method 2

src = input('Enter source file')

with open(src, "r") as input_file, \
     open('results.txt', 'w') as output_file:

    for line in input_file:
        if "error" in line:
            output_file.write(line)