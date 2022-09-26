import matplotlib.pyplot as plt
x_value=range(1,1001)
y_value=[x**2 for x in x_value]
plt.style.use ('seaborn-v0_8')
fig,ax=plt.subplots()
ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.viridis,s=10) #s 是点点的大小尺寸
ax.axis([0,1100,0,1100000])
plt.show()