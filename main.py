import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint


def logistic(x, t):

    return x * (1 - x)


ts = np.linspace(0.0, 10.0, 100)
x0 = 0.5
xs = odeint(logistic, x0, ts)

plt.xlabel("$t$", fontsize=16)
plt.ylabel("$x$", fontsize=16)
plt.plot(ts, xs)
plt.savefig("autonomous", dpi=300)
plt.show()


def logistic(x, t):

    return x * (1 - x)


ts = np.linspace(0.0, 10.0, 100)
lcs = np.linspace(0.0, 2.01, 20)

for x0 in lcs:
    xs = odeint(logistic, x0, ts)
    plt.plot(ts, xs)

plt.xlabel("$t$", fontsize=16)
plt.ylabel("$x$", fontsize=16)
plt.plot(ts, xs)
plt.savefig("different initial conditions", dpi=300)
plt.show()
