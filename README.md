# Colorblind-friendly matplotlib.pyplot style

The 'matplotlib' library is an amazing tool to produce visualizations
in Python.  However, produing colorblind-friendly plots, while
possible, require lots of tweakings. This package aims at simplifying
this step. Here is a global comparison of default style, new style and
colorblind style, each time displaying along the same graph without
the colors:

<img src="https://github.com/RichardSartori/CBPlot/figures/compare_all.pdf" width="960">

# Usage

```python
for i in range(3):
	X = np.linspace(0, 1, 15)
	Y = X + i/2
	plt.plot(X, Y)
```
will plot:
<img src="https://github.com/RichardSartori/CBPlot/figures/default.pdf" width="400">

```python
import styles
style_iterator = styles.styles(True)
for i in range(3):
	X = np.linspace(0, 1, 15)
	Y = X + i/2
	style = next(style_iterator)
	plt.plot(X, Y, **style)
```
will plot:
<img src="https://github.com/RichardSartori/CBPlot/figures/using_styles.pdf" width="400">