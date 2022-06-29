import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8]) #grafiğin kaplayacağı alanı belirledik
diller = ["C","CPP","PYTHON"]
sayi = [20,25,50]
ax.bar(diller,sayi)
plt.show()