import matplotlib.pyplot as plt
from randam_walk import RandomWalk
rw=RandomWalk()
rw.fill_walk()
plt.style.use('classic')
fig,ax=plt.subplots()
point_numbers=range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values, c=point_numbers, cmap=plt.cm.viridis, edgecolor='none',s=15)   #彩色显示

plt.show()