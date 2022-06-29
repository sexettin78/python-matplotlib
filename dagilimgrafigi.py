import matplotlib.pyplot as plt
kiz_not = [75,65,90,20,50,60,70,80,90,5]
erkek_not = [80,5,60,15,100,1,4,5,7,8]
not_Aralik = [10,20,30,40,50,60,70,80,90,100]

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.scatter(not_Aralik, kiz_not, color='r')
ax.scatter(not_Aralik, erkek_not, color='b')

ax.set_title("not dağılımı")
ax.set_xlabel('sınıf')
ax.set_ylabel('alınan not')
plt.show()