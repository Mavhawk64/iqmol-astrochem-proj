import pyautogui as pg
import os

functionals = []
methods = []
with open("C:/Users/mavbe/Desktop/Coding Folder/repos/iqmol-astrochem-proj/functionals.txt", "r") as f:
    functionals = f.readlines()
    f.close()

with open("C:/Users/mavbe/Desktop/Coding Folder/repos/iqmol-astrochem-proj/methods.txt", "r") as f:
    methods = [i.strip() for i in f.readlines()]
    f.close()

print(pg.position())

index = 9

job_section = (325, 106) # dropdown
calculate = (325, 137) # dropdown
method = (275, 160) # dropdown / text --> fill in the functional here [i.e., double click to highlight, then type]
basis = (325, 190) # dropdown
exchange = (325, 216) # dropdown
charge = (575, 138) # number
multiplicity = (575, 163) # number
ecp = (647, 188) # dropdown
correlation = (647, 218) # dropdown
new_job = (580, 106) # button
submit = (1862, 954) # button
job_rem = (927, 216)
job_end = (1000, 400)
some_button = (54, 605)

if __name__ == "__main__":
    pg.click(job_rem)
    # ctrl+a & delete
    pg.hotkey('ctrl', 'a')
    pg.press('delete')

    with open("C:/Users/mavbe/Desktop/Coding Folder/repos/iqmol-astrochem-proj/outline.txt", "r") as f:
        lines = [i.replace('{functional}', methods[index]) for i in f.readlines()]
        f.close()

    for line in lines:
        pg.typewrite(line)
    
    pg.sleep(0.5)
    # click on submit
    pg.click(submit)
    # type h2o2_geo_opt_{functionals[index]}
    pg.typewrite(f"h2o2_freq_{functionals[index].lower()}")
    # make directory
    if not os.path.exists(f"C:/Users/mavbe/Desktop/Coding Folder/repos/iqmol-astrochem-proj/molecule/output/h2o2_freq_{functionals[index].strip().lower()}"):
        os.mkdir(f"C:/Users/mavbe/Desktop/Coding Folder/repos/iqmol-astrochem-proj/molecule/output/h2o2_freq_{functionals[index].strip().lower()}")
        