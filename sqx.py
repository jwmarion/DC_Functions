#sqx.py
import matplotlib.pyplot as plot

def f(x):
    return x * x


xs = range(-100, 100)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
