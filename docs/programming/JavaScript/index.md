# JavaScript
## Basics
### Cloning an object
There are several ways to create a copy of an object, and depending on what you want, you can choose between shallow or deep copies[^shallow-deep][^shallow-deep2]. 

**NOTE:** By default, JavaScript passes everything by reference, so modifying one property as part of the new instance, will result in it being changed in the original object as well.

``` javascript
a = { test:42 };
b = a; // does not create a copy
c = { ...a }; // creates a shallow copy
d = Object.assign({}, a); // creates a shallow copy
e = JSON.parse( JSON.stringify(a); // creates a deep copy
```

[^shallow-deep]: [Understanding Deep and Shallow Copy in Javascript](https://we-are.bookmyshow.com/understanding-deep-and-shallow-copy-in-javascript-13438bad941c)

[^shallow-deep2]: [Explanation of Deep and Shallow Copying](https://www.cs.utexas.edu/~scottm/cs307/handouts/deepCopying.htm)