#tempConvert.py


import matplotlib.pyplot as plot

temp = int(raw_input("Enter a temp in celcius: "))

def f(x):
    return (x * 1.8) + 32

xs = range(temp -5, temp + 5, 1)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
