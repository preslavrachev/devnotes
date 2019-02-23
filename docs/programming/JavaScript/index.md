# JavaScript
## Basics
### String Manipulation
#### Replacing all occurences of a String
Whoever has tried `String.replace()` knows that it would remove the first occurence of the string you want to replace. That is, unless you use a regular expression[^replace]:

```javascript
"2019-08-07".replace("-", "/"); // => 2019/08-07
"2019-08-07".replace(/-/g, "/"); // => 2019/08/07
```
The trick is to apply the `g` flag to the regex, telling it to apply the change across the entire string. If the regex becomes more comple, you might consider compiling it and storing it in a variable[^regex].

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

[^replace]: [How to replace all occurrences of a string in JavaScript | StackOverflow](https://stackoverflow.com/a/1144788/1107412)

[^regex]: [Creating a regular expression | Mozilla Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)

[^shallow-deep]: [Understanding Deep and Shallow Copy in Javascript](https://we-are.bookmyshow.com/understanding-deep-and-shallow-copy-in-javascript-13438bad941c)

[^shallow-deep2]: [Explanation of Deep and Shallow Copying](https://www.cs.utexas.edu/~scottm/cs307/handouts/deepCopying.htm)