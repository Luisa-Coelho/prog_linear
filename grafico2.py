import matplotlib.pyplot as plt
import numpy as np

# plot the feasible region

#x1,x2 = np.meshgrid(d,d)
#plt.imshow( ((y>=2) & (2*y<=25-x) & (4*y>=2*x-8) & (y<=2*x-5)).astype(int), extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);#
#n_rest = int(input("insera a qtde de rest"))
#rest = []
#for i in range(0, n_rest):
#    restricoes = int(input(f"INSIRA A RESTRICAO {n_rest}"))
#    rest.append(restricoes)

d = np.linspace(0,2000,2000)
x, y = np.meshgrid(d,d)
#if n_rest == 1:
#    plt.imshow( ((rest[0])).astype(int), extent=(x.min(),x.max(),y.min(),y.max()), origin="lower", cmap="Greys", alpha = 0.3)
#if n_rest == 2:
#    plt.imshow( ((rest[0]) & (rest[1])).astype(int), extent=(x.min(),x.max(),y.min(),y.max()), origin="lower", cmap="Greys", alpha = 0.3)

plt.imshow( ((y<= 200 - 2*x) & (3*y <= 300 - x)).astype(int), extent=(x.min(),x.max(),y.min(),y.max()), origin="lower", cmap="Greys", alpha = 0.3)

# plot the lines defining the constraints
x = np.linspace(0, 2000, 2000)
x2 = np.linspace(2000, 2000, 2000)

# 2x1+x2 = 200
y1 = 200 - 2*x

# 2x1+x2 = 200
#x1 = 200 - y

# x1 + 3x2 = 300
y2 = x - 300

# x1 + 3x2 = 300
#x2 = -3*y -300

# Make plot
plt.plot(x, y1, label=r'$2y\leq25-x$')
plt.plot(x, y2, label=r'$4y\geq 2x - 8$')

plt.xlim(0,500)
plt.ylim(0,500)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.show()