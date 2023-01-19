import sys, argparse
import os 
import shutil
import subprocess




def FAIMS_splitter(in_raw,out_raw=None):
    all_files=os.listdir(in_raw)
    if out_raw != None:
         os.makedirs(out_raw)
    else:
        out_raw=in_raw
    raw_files=[file for file in all_files if ".raw" in file]
    os.makedirs("temp_split2",exist_ok=True)
    for raw in raw_files:
        print(raw)
        raw_path=os.path.join(in_raw,raw)
        temp_path=os.path.join(os.getcwd(),"temp_split2",raw)
        print(temp_path)
        shutil.copy(raw_path,temp_path)
    raw_grab=os.path.join(os.getcwd(),"temp_split2","*")
    slice_out=os.path.join(os.getcwd(),out_raw)
    # p=subprocess.Popen(f"ThermoFAIMStoMzML.exe {raw_grab} -o {slice_out}", shell=True)
    p=subprocess.Popen(f"ThermoFAIMStoMzML.exe", shell=True)
    print(p)
    os.rmdir("temp_split2")


FAIMS_splitter("C:\\Users\\tcoop\\Desktop\\Target_Folder")
