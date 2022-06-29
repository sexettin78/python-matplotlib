import numpy as np
import matplotlib.pyplot as plt
xlist = np.linspace(-5.0,5.0,50)
ylist = np.linspace(-5.0,5.0,50)
x,y = np.meshgrid(xlist,ylist)
z = np.sqrt(x**2 + y**2)
fig,ax = plt.subplots(1,1)
cp = ax.contourf(x,y,z) #dolgu yapıldı
fig.colorbar(cp)  #çizgiler çekildi
ax.set_title('kontur grafiği')
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()