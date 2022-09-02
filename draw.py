import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))

x1 = [[30, 30], [0, 250], [0, 130], [130, 130], [80, 80], [0, 170], [220, 220], [30, 130], [180, 180], [130, 220],
      [130, 220]]
y1 = [[0, 250], [30, 30], [80, 80], [0, 250], [30, 80], [220, 220], [170, 0], [130, 130], [30, 160], [160, 160],
      [90, 90]]

for i in range(len(x1)):
    plt.plot(x1[i], y1[i], 'g-', linewidth=5.0)

x2 = [[30, 30]]
y2 = [[85, 215]]

for i in range(len(x2)):
    plt.plot(x2[i], y2[i], 'y-', linewidth=5.0)

x3 = [[30, 130]]
y3 = [[130, 130]]

for i in range(len(x3)):
    plt.plot(x3[i], y3[i], 'r-', linewidth=5.0)

plt.xlim(0, 250)
plt.ylim(0, 250)
plt.show()
