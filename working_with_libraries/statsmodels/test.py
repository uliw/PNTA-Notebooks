import pathlib as pl 
import pandas as pd

fn: str = "Mg_Ca_S2b1_BeecheyIsland.xlsx"  # file name
sn: str = "Mg_Ca_complete"  # sheetname
cwd :pl.Path = pl.Path.cwd() # get the current working directory
fqfn :pl.Path = pl.Path(f"{cwd}/{fn}") # fully qualified file name

if not fqfn.exists():  # check if file exist
    raise FileNotFoundError(f"Cannot find file {fqfn}")

df: pd.DataFrame = pd.read_excel(fqfn, sheet_name=sn) # read csv data

x = df. iloc[:, 0]
y = df. iloc[:, 1]
