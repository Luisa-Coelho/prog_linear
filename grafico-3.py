import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy
from numpy import arange


figure()
#A = arange(-10, 20, 2)  ## FUNÇÃO
#B = arange(-10, 20, 2)

# constraint equation

#B1 = 20.0 - A

#xlim = (-100, 220)
#ylim= (-100, 220)
hlines(0, -10, 20, color = 'k')
vlines(0, -10, 20, color = 'k')
grid(True)

xlabel('X-axis')
ylabel('Y-axis')

#Plotting graph
x1 = [2.5, 0]
x2 = [0, 3.33]

x3 = [10, 0]
x4 = [0, 10]
plot(x1, x2, color = 'b')
plot(x3, x4, color = 'b')
#axhline(y = 10, color = 'r')  ## restricao do tipo x2 = 10
#axvline(x = 3.33, color = 'r')


#title('objective function: z = 5000B - 2000A with following constarints')
#legend(['A+B>=200','200>=A>=100','170>=B>=80'])

# get the co-ordinates of intersection points by mere visualisation
A = [2.5, 0, 0.00, 0.00]
B = [0.00, 3.33, 0.00, 0.0]
fill(A,B,'g+')

#c = [0, 10, 10, 7.5]
#d = [10, 0, 6.67, 10]
#fill(c,d,'b+')

e = [0, 10, 2.5, 0]
f = [10, 0, 0, 3.33]
fill(e,f,'r+')




show()