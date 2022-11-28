import statsmodels.formula.api as smf
import pandas as pd  # import pandas as pd
import pathlib as pl


fn: str = "storks_vs_birth_rate.csv"  # file name
cwd: pl.Path = pl.Path.cwd()
fqfn: pl.Path = pl.Path(f"{cwd}/{fn}")
if not fqfn.exists():  # check if the file is actually there
    raise FileNotFoundError(f"Cannot find file {fqfn}")

df: pd.DataFrame = pd.read_csv(fn)  # read data
df.columns = ["Babies", "Storks"]  # replace colum names

model: smf.ols = smf.ols(formula="Babies ~ Storks", data=df)
results :model.fit
results: model.fit = model.fit()  # fit the model to the data
print(results.summary())  # print the results of the analysis
