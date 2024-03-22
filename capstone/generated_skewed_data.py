import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import skewnorm
# mpl.use("TkAgg")

# Generate random data between

a=10
# x_noise = skewnorm.rvs(a, size=100)
y_noise = skewnorm.rvs(a, size=100)
x_noise = np.random.uniform(low=-1, high=1, size=(100,))

x_data = np.linspace(1, 10, 100)
y_data = np.linspace(1, 10, 100)

x = x_data + x_noise
y = y_data + y_noise


plt.style.use("uli")
fig, ax = plt.subplots()
ax.scatter(x, y, color="C0")
fig.savefig("test_figure.pdf")
plt.show()
df = pd.DataFrame({"X": x, "Y": y})
df.to_csv("y_skewed.csv", index=False)
