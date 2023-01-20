import os 
import subprocess
import json




def FAIMS_splitter(in_raw,out_raw=None):
    if out_raw != None:
         os.makedirs(out_raw)
         slice_out=out_raw
    else:
        out_raw=in_raw
        slice_out=in_raw
    raw_grab=os.path.join(in_raw,"*")
    p=subprocess.Popen(f"C:\\Users\\tcoop\\Desktop\\FAIMS_Splitter\\ThermoFAIMStoMzML.exe {raw_grab} -o {slice_out}", shell=True)
    # p=subprocess.Popen(f"ThermoFAIMStoMzML.exe", shell=True)
    print(p)


FAIMS_splitter("C:\\Users\\tcoop\\Desktop\\Target_Folder")

with open("FAIMS_DDA.fp-manifest", "r") as manifest:
    x=manifest.read()
    print(type(x))
    print(x)
    print("\n")
    x_table = x.strip().splitlines()
    print(x_table)
    x_table2=[x.split("\t") for x in x_table]
    print(type(x_table2))
    print(x_table2)

def gen_manifest(in_dir, bioreplicate=1, acq_type="DDA"):
    temp_list= [file for file in os.listdir(in_dir) if ".mzML" in file]
    name_list= [name.split(".")[0] for name in temp_list]
    path_list=[]
    for file, name in zip(temp_list,name_list):
        biorep=str(bioreplicate)
        file2=in_dir+"\\"+file
        path_name=f"{file2}"+"\t"+f"{name}"+"\t"+f"{biorep}"+"\t"+f"{acq_type}"
        path_list.append(path_name)
    path="\n".join(path_list) 
    print(path)   
    with open("Test.fp-manifest","w") as manicure:
        manicure.write(path)
        manicure.close()

gen_manifest("C:\\Users\\tcoop\\Desktop\\Target_Folder")



temp_file="FAIMS_DDA_LFQ2.workflow"
# def gen_workflow(in_file):
with open(f"{temp_file}", "r") as workflow:
    x=workflow.read()
    x_table = x.strip().splitlines()
    workflow.close()
table_dic={}
table3a=[table for table in x_table if  "Workflow" in table]
for s in table3a:
    key1=s.split(":")[0]
    value1=s.split(":")[1]
    table_dic[key1]=value1
table_dic={s.split(":") for s in table3a}
table3b=[table for table in x_table if "=" in table]
for s in table3b:
    key2=s.split("=")[0]
    value2=s.split("=")[1]
    table_dic[key2]=value2
print(table_dic)
with open(f"{value1}.json","w") as outfile:
            Jstring=json.dumps(table_dic)
            outfile.write(Jstring)
            outfile.close()
    # return table_dic

# gen_workflow(temp_file)

def mod_workflow(input):
    if isinstance(input, dict)==True:
        print("Dictionary Recieved")
    elif ".json" in input:
        print("JSON FILE Recieved")
    else:
        print("Provide dictionary or JSON for input variable")

