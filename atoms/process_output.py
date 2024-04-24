import os
import json
functionals = []
with open("C:/Users/mavbe/Desktop/Coding Folder/repos/iqmol-astrochem-proj/functionals.txt", "r") as f:
    functionals = [i.strip() for i in f.readlines()]
    f.close()
pwd = "C:/Users/mavbe/Desktop/Coding Folder/repos/iqmol-astrochem-proj/atoms"
atoms = ["magnesium", "fluorine"]
paths = [{"ground": f"{pwd}/output/{atom}/{atom}.out", "excited": f"{pwd}/output/{atom}_excited/{atom}_excited.out"} for atom in atoms]
j=  0
for path in paths:
    atom = atoms[j]
    j += 1
    with open(path["ground"], "r") as f:
        lines = f.readlines()
        f.close()
    with open(path["excited"], "r") as f:
        linez = f.readlines()
        f.close()

    # search for len(functionals) * "Total energy =  "
    energies = {}
    i = 0
    for line in lines:
        if "Total energy =  " in line:
            energies[functionals[i]] = {"ground_state": line.split()[-1]}
            i += 1
    i = 0
    for line in linez:
        if "Total energy =  " in line:
            energies[functionals[i]]["excited_state"] = line.split()[-1]
            i += 1
    
    # find the difference between each functional's ground and excited state energies
    for functional in functionals:
        energies[functional]["difference"] = str(float(energies[functional]["excited_state"]) - float(energies[functional]["ground_state"]))

    # output to json
    with open(f"{pwd}/{atom}_energies.json", "w") as f:
        f.write(json.dumps(energies, indent=4))
        f.close()