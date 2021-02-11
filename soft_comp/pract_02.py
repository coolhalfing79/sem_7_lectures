import numpy as np
import matplotlib.pyplot as plt
from neuron import *


plt.style.use('seaborn')
fig, axs = plt.subplots(nrows=3, ncols=3)
ax = axs.flatten()
# plt.figure(constrained_layout=True)
x = np.linspace(-10, 10, 1000)

y = signum(x)
ax[0].set_title('signum')
ax[0].plot(x, y)

y = bipolar_step(x)
ax[1].set_title('bipolar signum')
ax[1].plot(x, y)

y = u_sigmoidal(x)
ax[2].set_title('sigmoidal')
ax[2].plot(x, y)

y = b_sigmoidal(x)
ax[3].set_title('bipolar\nsigmoidal')
ax[3].plot(x, y)

y = hyperbolic_tan(x)
ax[4].set_title('hyperbolic\ntan')
ax[4].plot(x, y)

y = arctan(x)
ax[5].set_title('arctan')
ax[5].plot(x, y)

y = relu(x)
ax[6].set_title('relu')
ax[6].plot(x, y)

y = leaky_relu(x)
ax[7].set_title('leaky relu')
ax[7].plot(x, y)

y = b_peicewise_linear(x)
ax[8].set_title('bipolar\npeicewise linear')
ax[8].plot(x, y)

fig.tight_layout()
plt.show()