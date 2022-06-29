import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8]) #grafiğin kaplayacağı alanı belirledik
diller = ["C","CPP","PYTHON"]
sayi = [20,25,50]
ax.pie(sayi, labels = diller, autopct="%1.2f%%") #virgülden sonraki 2 basamağa kadar göster dedik
plt.show()