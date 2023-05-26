import styles
import numpy as np
import matplotlib.pyplot as plt

N = 3
X = np.linspace(0, 1, 15)

plt.figure("default")
for i in range(N):
	Y = X + i/2
	plt.plot(X, Y)

plt.figure("using_styles")
style_iterator = styles.styles(True)
for i in range(N):
	Y = X + i/2
	style = next(style_iterator)
	plt.plot(X, Y, **style)

plt.show()
