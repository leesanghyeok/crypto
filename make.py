import os
import sys
#show the file list in current directory
curdir = os.getcwd()
pathlist = [f for f in os.listdir(curdir) if os.path.isfile(os.path.join(curdir,f)) and os.path.splitext(f)[1]=='.py' and f!='make.py']
#read and show the file
textlist = []
for i in pathlist:
    f = open(os.path.join(curdir,i),'r')
    textlist.append(f.read())
    f.close()

#put the texts together
output = "".join(textlist)
if len(sys.argv)==2:
    filename = sys.argv[1]
else:
    filename = "default.py"

f = open(os.path.join(curdir,filename),'w')
f.write(output)
f.close()
