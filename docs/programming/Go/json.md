# JSON Manipulation

## Frequently Asked Questions
### When should I use `json.Decode` and when `json.Unmarshall`?

`Decode` uses `Unmarshall` under the hood, but takes the concrete decoder into consideration. 

Here is a simple rule of thumb:

- Use `json.NewDecoder(...).Decode()` if your data is coming from an io.Reader stream, or you need to decode multiple values from a stream of data.
- Use `json.Unmarshal` if you already have the JSON data in memory.

Usually, you would try to convert the response of an HTTP request to a JSON object, in which case `Decode` is the better choice:

```go
json.NewDecoder(res.Body).Decode(&myResponseStruct{})
```


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
