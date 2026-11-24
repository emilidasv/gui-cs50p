import filecmp
from os import getcwd

mypath = getcwd()+'/myfile/from/the/base/directory/this/gets/executed'

f1 = input("give path to first file")
f2 = input("give path to secondfile")
#f1 = "textfile_1.txt"
#f2= "textfile_2.txt"



# shallow comparison
result = filecmp.cmp(f1, f2)
print(result)
# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)
