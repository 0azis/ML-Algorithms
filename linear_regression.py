# The code of linear regression

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


x = np.random.randint(100, size=10)
y = np.random.randint(100,size=10)

lreg = stats.linregress(x, y)
print(lreg)

plt.scatter(x, y)
plt.plot(x, lreg.intercept + lreg.slope*x)
plt.show()