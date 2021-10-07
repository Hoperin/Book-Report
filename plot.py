import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import ticker


plt.ylim(0, 20)
plt.xlim(0, 365)

data1 = np.random.random([6,50])
colors1 = ['C{}'.format(i) for i in range(6)]

lineoffsets1 = [-15, -3, 1, 1.5, 6, 10]
linelengths1 = [5, 2, 1, 1, 3, 1.5]

fig, axs = plt.subplots()

axs.eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)

plt.show()