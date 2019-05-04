import ast,_ast
from plagiarism.views import getfile1,getfile2
from plagiarism.file3 import compare
from plagiarism.lines import length1
from plagiarism.lines import length
from django.shortcuts import render
#getfile1()
#getfile2()
#from .views import getfile
#fileres1=getfile()
#open('file1.py', 'w').close()
#open('file2.py', 'w').close()
#open('file1_dump.py', 'w').close()
#open('file2_dump.py', 'w').close()
open('file1_funcDef.py', 'w').close()
open('file2_funcDef.py', 'w').close()
file1=ast.parse(open('file1.py').read())
print("First File is read and parsed")
file2=ast.parse(open('file2.py').read())
print("Second file is read and parsed")
file1_dump=ast.dump(file1,annotate_fields=False,include_attributes=True)
with open('file1_dump.py','wt')as f1:
    f1.write(file1_dump)
file2_dump = ast.dump(file2,annotate_fields=False,include_attributes=True)
with open('file2_dump.py','wt')as f2:
    f2.write(file2_dump)
f7=open('file1_dump.py','r')
f8=open('file2_dump.py','r')
#FO = open('op_funcDef.txt', 'w')

def sameprog():
    open('file1_dump.py', 'w').close()
    open('file2_dump.py', 'w').close()
    file1=ast.parse(open('file1.py').read())
    file2=ast.parse(open('file2.py').read())
    file1_dump=ast.dump(file1,annotate_fields=False,include_attributes=True)
    with open('file1_dump.py','wt')as f1:
        f1.write(file1_dump)
    file2_dump = ast.dump(file2,annotate_fields=False,include_attributes=True)
    with open('file2_dump.py','wt')as f2:
        f2.write(file2_dump)
    f7=open('file1_dump.py','r')
    f8=open('file2_dump.py','r')
    count=0
    value=False
    for line1 in f7:
        for line2 in f8:
            if (line1==line2):
                count=count+1
                value=True
                data="same programs"
            else:
                value=False
                data="not same programs"
    return data


#for node in ast.walk(file1):
 #   if isinstance(node, _ast.Call):
  #      string1=node.func.id
   #     with open('file1_funcDef.py','a') as f3:
    #        f3.write(string1)
#for node in ast.walk(file2):
 #   if isinstance(node, _ast.Call):
  #      string2=node.func.id
   #     with open('file2_funcDef.py','a') as f4:
    #        f4.write(string2)
f5=open('file1_dump.py','r')
f6=open('file2_dump.py','r')
#FO = open('op_funcDef.txt', 'w')
for line1 in f5:
    for line2 in f6:
        if (line1==line2):
           print("same functions")
        else:
            print("not same functions")
names = sorted({node.id for node in ast.walk(file1) if isinstance(node, ast.Name)})
print(names)
names1 = sorted({node.id for node in ast.walk(file2) if isinstance(node, ast.Name)})
print(names1)
if(names==names1):
    print("same function and variable names")
else:
    print("different function and variable names")
compare()
print("------------------")
def percent(request):
    getfile1()
    getfile2()
    f7 = open('file1.py', 'r')
    f8 = open('file2.py', 'r')
    # FO = open('op_funcDef.txt', 'w')
    count1 = 0
    g1 = set(line.strip() for line in open('file1.py'))
    g2 = set(line.strip() for line in open('file2.py'))
    for line in g1 & g2:
        if line:
            count1 = count1 + 1
            print(line)
    print("no of similar lines: ")
    count=count1+2
    print(count)
    a=length()
    a1=length1()
    print("number of lines in file1 and file2: ")
    print(a,a1)
    #print("common number of lines:")
    #print(count1)
    b=count/a*100
    samepr=sameprog()
    print(samepr)
    print("percentage :")
    print(b)
    samepr+=str(' ')
    samepr+=str(b)
    #return (samepr)
    return render(request,'plagiarism/page3.html',{'data':samepr})
#print(percent())
print("--------------------")
data=sameprog()
print(data)

