# JSON Manipulation

## 3rd Party Libraries
### GJSON
[GJSON](https://github.com/tidwall/gjson) provides a fast and simple way to get values from a json document. It has features such as one line retrieval, dot notation paths, iteration, and parsing json lines.

A basic example from the GJSON README:

``` go
package main

import "github.com/tidwall/gjson"

const json = `{"name":{"first":"Janet","last":"Prichard"},"age":47}`

func main() {
	value := gjson.Get(json, "name.last")
	println(value.String())
}
```
