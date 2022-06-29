import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(311) #satır sütun konum
ax1.plot([1,2,3])
ax1.plot(range(20,50)) #0'dan 50'ye kadar olan sayılardan 1'er artarak oluşacak
plt.show()