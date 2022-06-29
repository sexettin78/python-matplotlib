import matplotlib.pyplot as plt
import numpy as np
import math 
x= np.arange(0, math.pi*2,0.05)
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
y = np.sin(x)
ax.plot(x,y)
ax.set_xlabel("x ekseni")
ax.set_ylabel("y ekseni")
ax.set_title("sin")
ax.set_xticks([0,2,4,6])
ax.set_xticklabels(['sıfır','iki','dört','altı'])
ax.set_yticks([-1,0,1])
plt.show()
#0-2-4-6 yerine sıfır-iki-dört-altı yazdırdık