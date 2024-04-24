import os
import json


pwd = "C:/Users/mavbe/Desktop/Coding Folder/repos/iqmol-astrochem-proj/molecule"
molecule = "h2o2"
functionals = ["B3LYP", "BLYP", "CAM-B3LYP", "HF", "M06-2X", "Omega-B97X-D", "PBE", "PBE0", "revPBE", "TPSS"]
paths = [f"{pwd}/output/{molecule}_freq_{functional.strip().lower()}/{molecule}_freq_{functional.strip().lower()}.out" for functional in functionals]

output = {}

for i, path in enumerate(paths):
    with open(path, "r") as f:
        lines = f.readlines()
        f.close()
    
    # search for  Frequency:       326.75                1391.66                1459.83
    #             Frequency:      1701.47                3496.23                3534.43
    # six modes
    frequencies = []
    for line in lines:
        if "Frequency:" in line:
            frequencies.extend(line.split()[1:])
    
    output[functionals[i]] = {"frequencies": frequencies}

# output to json
with open(f"{pwd}/{molecule}_frequencies.json", "w") as f:
    f.write(json.dumps(output, indent=4))
    f.close()