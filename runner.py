import pyautogui as pg

functionals = []
with open("functionals.txt", "r") as f:
    functionals = f.readlines()
    f.close()

# print(pg.position())

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

if __name__ == "__main__":
    for i in range(len(functionals)):
        # click on the method and type the functional
        pg.click(method)
        # ctrl+a & delete
        pg.hotkey('ctrl', 'a')
        pg.press('delete')
        # type the functional
        pg.typewrite(functionals[i])
        # click on the new job button
        if i != len(functionals) - 1:
            pg.click(new_job)