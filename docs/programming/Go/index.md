# Introduction

## Basics

### Pass-by-reference

In Go, there is no implicit _pass-by-reference_. Everything is **a value**, unless using a pointer[^pass-by-value][^pass-by-value2].

```go
package main

import "fmt"

type Person struct {
	Name string
}

func passByVal(person Person) Person {
	// changing the name won't have an effect on the original variable
	person.Name = "John Smith"
	return person
}

func passByRef(person *Person) *Person {
	// changing the name will have an effect on the original variable
	person.Name = "John Smith"
	return person
}

func main() {
	me := Person{Name: "Preslav Rachev"}
	fmt.Println(me)
	fmt.Println(passByVal(me))
	fmt.Println(me)
	fmt.Println(*passByRef(&me))
	fmt.Println(me)
}
```

will result in the following output:

```
{Preslav Rachev}
{John Smith}
{Preslav Rachev}
{John Smith}
{John Smith}
```

### Generics

Go does not have generics, the way other languages do. Frankly, because of the complexity they introduce. This is not to say that you cannot acieve some sort of type of formal restrictions, but mainly, using Go's native constructs[^generics].

### Readers and Writers

#### Writers

```go
type Writer interface {
    Write(p []byte) (n int, err error)
}
```

##### Passing a string to a writer
Often, you will need to conver a string to a slice of bytes, in order to pass it to a `Writer`. The easiest way to do this in Go, is using simple type conversion. The code in the following example will write the string "Hello World!" to an HTTP `ResponseWriter` instance, which is technically a `Writer`, since it implements the `Write` method.

```go
http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello World!"))
})
```

## Databases

### SQLite

#### Drivers

[https://github.com/mattn/go-sqlite3](https://github.com/mattn/go-sqlite3) supports database/sql, based on cgo.
[https://github.com/feyeleanor/gosqlite3](https://github.com/feyeleanor/gosqlite3) doesn't support database/sql, based on cgo.
[https://github.com/phf/go-sqlite3](https://github.com/phf/go-sqlite3)

[Building Web application with Golang](https://astaxie.gitbooks.io/build-web-application-with-golang/en/05.3.html)

[^pass-by-value]: [When are function parameters passed by value? | The Go Programming Language FAQ](https://golang.org/doc/faq#pass_by_value)
[^pass-by-value2]: [There is no pass-by-reference in Go | Dave Cheney](https://dave.cheney.net/2017/04/29/there-is-no-pass-by-reference-in-go)
[^generics]: [Who needs generics? Use ... instead!](https://appliedgo.net/generics/)

## Backend Development

[Building a RESTful API in Go Using Only the Standard Library](https://www.goin5minutes.com/screencast/episode_1_building_restful_api_using_only_std_lib/)
