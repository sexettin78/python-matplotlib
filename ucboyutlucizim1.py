from matplotlib import projections
from mpl_toolkits import mplot3d #grafiğin 3d olmasını sağlamak için
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d") #3 boyut için projection="3d" gerekli
z = np.linspace(0,1,50)
x = z*np.sin(10*z)
y = z*np.cos(10*z)
ax.plot3D(x,y,z,'gray') #çizdirme işlemi yapıldı
ax.set_title("grafik başlığı")
plt.show()