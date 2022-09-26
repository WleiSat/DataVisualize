import matplotlib.pyplot as plt
x_value=range(1,1001)
y_value=[x*x*x for x in x_value]
plt.style.use ('seaborn-v0_8')
fig,ax=plt.subplots()
ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.viridis,s=10) #s 是点点的大小尺寸
ax.axis([0,1002,0,1300000000])
plt.show()