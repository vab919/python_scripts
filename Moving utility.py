'##This project copies files from a source directory to a destination directory'
import os
import shutil
import sys
os.chdir("C:\\Users\\210804\\Desktop")

#src = (os.getcwd())

src = input('Enter source folder')

print('After changing directory, the current directory is %s' % src)
dest = input('Enter destination folder')

print(os.listdir(src))
src_files = os.listdir(src)

print(src_files)
for file_name in src_files:
     full_file_name = os.path.join(src, file_name)
     if (os.path.isfile(full_file_name)):
         shutil.copy(full_file_name, dest)


# print(os.environ.get)

#print(getURL(4,9))

# os.chdir('c:\\users\\210804\\desktop')
#
# workbook = openpyxl.load_workbook('PT.xlsx')
#
# type(workbook)
#
# #sheet = workbook.get_sheet_names()
#
# print('hi')

# num1 =1
# num2 =10
#
# print(num1+num2)
#
# string1 ='Vaibhav'
#
# print(string1)
#
# print('string1+num1')
#
# num= int(input('Enter the value of n='))
# if (num <=0)< =0:
#     print(Enter value great than 0)
# else:
#     sum=0
#     while(num>0):
#         sum+=num
#
#         print(sum)
# while(i<10):
#     print(i=i+`)
#a=100
#print(a)

#
#
# Number1=int(input('Hi VIhaan , Enter the first number you would like to add'))
#
# Number2=int(input('Okay VIhaan! Now, enter the second number'))
#
# print('Here is your addition answer b uddy')
# print(int(Number1+Number2))

# def fibo(n):
#     a=0
#     b=1
#     for x in range(n):
#         a=b
#         b=a+b
#         print(a, '\n')
#     return b
# num = int(input("Enter value of n"))
#
# print(fibo(num))
# python -V