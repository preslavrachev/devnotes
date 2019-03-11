# NumPy

## Fitting a logarithmic curve 
There are times when you'd like to fit a logarithmic curve instead of a linear line. A good example is the relationship between house pricing and area. Though prices can go up indefinitely, housing area rarely deviates disproportionately from the mean.[^np_curve_fit]

```
import numpy as np

prices = np.array([1, 7, 20, 50, 79])
area = np.array([10, 19, 30, 35, 51])
np.polyfit(np.log(prices), area, 1)

# array([ 8.46295607,  6.61867463])
# ares ≈ 8.46 math.log(price) + 6.62
```

Alternatively, if you want to fit an exponential curve (e.g. the inverse relationship between are and price, simply reverse the order of the `x` and `y` arguments:

```
import numpy as np

prices = np.array([1, 7, 20, 50, 79])
area = np.array([10, 19, 30, 35, 51])
np.polyfit(area, np.log(prices), 1)

# array([ 0.01410343, 12.21866174])
# price ≈ 0.01410343 math.exp(area) + 12.21866174
```

[^np_curve_fit]: [How to do exponential and logarithmic curve fitting in Python? | StackOverflow](https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly)
