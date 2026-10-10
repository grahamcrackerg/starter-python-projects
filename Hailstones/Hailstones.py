import matplotlib.pyplot as plot

def hailstone(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(n)
    return sequence

x = list(range(1,1001))
y = [len(hailstone(n)) for n in x]
plot.scatter(x,y,color='blue', s=1)
plot.xlabel("Number")
plot.ylabel("Sequence Length")
plot.show()