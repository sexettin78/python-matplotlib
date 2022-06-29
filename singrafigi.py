from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05) #0'dan başlıyor 2 pi'ye kadar 0.05 artarak gidiyor
y = np.sin(x) #sinüs fonksiyonunu y değişkenine atadık
plt.plot(x,y)
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.title("sin grafiği")
plt.show()