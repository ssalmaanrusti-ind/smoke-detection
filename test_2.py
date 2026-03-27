import os
root="fine"
file_list=[]
for path, subdirs, files in os.walk(root):
    for name in files:
        tmp=(os.path.join(path, name))
        file_list.append(os.path.basename(tmp))

for xx in file_list:
    data=(xx.split("_"))
    data1=(xx.split("__"))
    name=data[0]
    date=data[1]+"_"+data[2]+"_"+data[3]
    time=data1[1]
    time = time.replace(".txt", "")
    print(name,date,time)
