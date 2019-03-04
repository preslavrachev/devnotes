# Pandas

## Simple Descriptive Statistics

Before taking the big guns, such as aggregations, I usually try to first get a good grasp of the data inside the data frame. Looking at the `head` and `tail` of the data framew is one of the first things you should do:

```python
# check the top of the data frame
df.head()

# check the botto of the data frame
df.tail()
```

If the data frame is very large you can also grab a random sample of it:

```python
# Fetch an exact number of random lines (make sure that freq=None)
df.sample(n=5)

# Fetch a percentage of random lines (make sure that n=None)
df.sample(freq=0.1)
```

Last but not least, you can try `describe` and `value_counts`. `describe` will return a new data frame consisting of various basic stats for each of the numeric columns in the data frame (count, mean, std, min, max, 25%, 50% 75%):

```python
df.describe()

#            price	area
#   count	150.0	150.000000
#   mean	943139.5	100.085800
#   std	    844677.0	44.566817
#   min	    62000.0	26.220000
#   25%	    419875.0	70.740000
#   50%	    585500.0	93.710000
#   75%	    1132500.0	126.697500
#   max	    4500000.0	279.500000
```

- [ ] ==**TODO:** Document `value_counts`==

`value_counts` gets applied applied to a discrete series instead, and is a really easy way of checking how many rows there of each value there are in a data frame:

```python
df["city"].value_counts()

#   München    96
#   Hamburg    24
#   Berlin     16
#   Bremen     14
```

## Encode categorical data
### Simple Encoding
There are many times, when you would need to turn your series of categorical data (e.g. city names, professions, car models, etc) into numeric representations. The simplest way to do this using Pandas, is to call `factorize` on the series you want to get encoded.[^factorize1][^factorize2]

!!! info "[factorize](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.factorize.html)"

	Encode the object as an enumerated type or categorical variable.
	This method is useful for obtaining a numeric representation of an array when all that matters is identifying distinct values. factorize is available as both a top-level function pandas.factorize(), and as a method 

```python
df['c_code'] = pd.factorize(df['city'])[0]

print(df)

#	 city      c_code
#  München  0
#  Bremen   1
#  Berlin   2
#  Hamburg  3
```

[^factorize1]: [Pandas: convert categories to numbers | Stackoverflow](https://stackoverflow.com/a/51311996/1107412)
[^factorize2]: [factorize | Pandas Docs](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.factorize.html)
