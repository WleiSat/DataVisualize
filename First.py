import matplotlib.pyplot as plt
sqares=[1,4,9,16,25]
input_values=[1,2,3,4,5]
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(input_values,sqares,linewidth=3)
plt.show()