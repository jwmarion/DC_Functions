#tempConvert.py

from numpy import arange
import matplotlib.pyplot as plot
import math
temp = int(raw_input("Enter a temp in celcius: "))

def f(x):
    return (x * 1.8) + 32


xs = arange(temp -10, temp + 10, 0.5)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
