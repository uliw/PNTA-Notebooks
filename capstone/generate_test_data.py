import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import shapiro
import statsmodels.api as sm

mpl.use("TkAgg")


# Generate random data between 0 an 1
rng = np.random.default_rng()
x_noise = rng.standard_normal(100)
y_noise = rng.standard_normal(100)  

x_data = np.linspace(1, 10, 100)
y_data = np.linspace(1, 10, 100)

x = x_data + x_noise
y = np.exp(y_data + y_noise)


# plt.style.use("uli")
# fig, ax = plt.subplots()
# ax.scatter(x, y, color="C0")
# fig.savefig("test_figure.pdf")
# plt.show()

fig, ax = plt.subplots()
sm.qqplot(x, ax=ax, line="s")
plt.show()

df = pd.DataFrame({"X": x, "Y": y})
df.to_csv("y_log.csv", index=False)
