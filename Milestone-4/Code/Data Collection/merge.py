import json

json_files=[]
for i in range(1, 32):
     json_files.append(str(i)+'output.json')

python_objects=[]

for json_file in json_files:
    with open (json_file,"r") as f:
        python_objects.append(json.load(f))

with open ("combined.json","w") as f:
        json.dump(python_objects,f)
        

