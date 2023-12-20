import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)
y=np.sin(x)
plt.figure()
plt.plot(x,y)
plt.title("Line chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

categories=['A','B','C','D']
values=[20,35,30,25]
plt.figure()
plt.bar(categories,values)
plt.title("Bar chart")
plt.xlabel("Categories")
plt.ylabel("Values")

x=np.random.randn(100)
y=np.random.randn(100)
colors=np.random.randn(100)
sizes=100*np.random.randn(100)
plt.figure()
plt.scatter(x,y,s=sizes,c=colors,alpha=0.5)
plt.title("Scatter plot")
plt.xlabel("X Axis")
plt.ylabel("Y axis")

sizes=[30,20,25,15,10]
labels=['A','B','C','D','E']
plt.figure()
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Pie chart")

plt.show()
