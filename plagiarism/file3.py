import ast
def compare():
    with open("file1.py",'r') as myfile1:
        data1=myfile1.read()
        length1=len(data1.split())
    print("number of tokens in file1: ")
    print(length1)
    with open("file2.py",'r') as myfile2:
        data2=myfile2.read()
        length2=len(data2.split())
    print("number of tokens in file2: ")
    print(length2)
    if(length1==length2):
        print("same number of tokens")
    else:
        print("different number of tokens")
compare()