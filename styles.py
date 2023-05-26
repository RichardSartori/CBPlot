import itertools as ijk

def styles(colorblind = False):
	"""
	return a generator over matplotlib line styles, as dicts
	each style is unique until the exhaustion of combinations
	if colorblind is true, uniqueness does not include the color
	generated dicts can be used with the **-operator when plotting
	matplotlib.pyplot.plot(X, Y, **dict)
	"""

	# subset of available specifiers
	colors = [ "C0", "C1", "C2", "C3" ]
	linestyles = [ "solid" ]
	markers = [ "None", "s", "o", "^" ]

	iterator = ijk.cycle(ijk.product(linestyles, markers, colors))

	if colorblind:
		linestyles += [ "dashed", "dashdot", "dotted" ]
		markers.remove("None")

		def unpack(arg):
			((a, b), c) = arg
			return (a, b, c)

		noncolor = ijk.cycle(ijk.product(linestyles, markers))
		iterator = map(unpack, zip(noncolor, ijk.cycle(colors)))

	for triplet in iterator:
		(l, m, c) = triplet
		yield { "linestyle":l, "marker":m, "color":c }

# usage example: plot comparison between styles
if __name__ == "__main__":

	import matplotlib.pyplot as plt
	import numpy as np

	def plot_sin_waves(axis, style_iterator, title):
		"""
		plot multiple sinus waves to axis and set title
		style used for each wave is taken from style_iterator
		"""
		axis.set_title(title)
		n_waves = 9
		X = np.linspace(0.0, 4.0*np.pi, 25)
		for i in range(n_waves):
			offset = i*(np.pi/n_waves)
			Y = np.sin(X-offset)
			style = next(style_iterator)
			axis.plot(X, Y, **style)

	def paint_it_black(style_iterator):
		"""
		return the same style_iterator except that
		every style has its color set to "black"
		"""
		for style in style_iterator:
			style["color"] = "black"
			yield style

	fig, axis = plt.subplots(3, 2)
	fig.suptitle("style comparison")
	default_style_iterator = ijk.repeat({})

	plot_sin_waves(axis[(0, 0)], default_style_iterator,
		"default matplotlib style, with colors")
	plot_sin_waves(axis[(0, 1)], paint_it_black(default_style_iterator),
		"default matplotlib style, without colors")
	plot_sin_waves(axis[(1, 0)], styles(),
		"styles(colorblind=False), with colors")
	plot_sin_waves(axis[(1, 1)], paint_it_black(styles()),
		"styles(colorblind=False), without colors")
	plot_sin_waves(axis[(2, 0)], styles(True),
		"styles(colorblind=True), with colors")
	plot_sin_waves(axis[(2, 1)], paint_it_black(styles(True)),
		"styles(colorblind=True), without colors")

	plt.show()
