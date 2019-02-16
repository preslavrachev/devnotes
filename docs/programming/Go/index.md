# Introduction

## Basics
### Pass-by-reference
In Go, there is no implicit _pass-by-reference_. Everything is **a value**, unless using a pointer[^pass-by-value][^pass-by-value2].

``` go
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

## Databases
### SQLite
#### Drivers

[https://github.com/mattn/go-sqlite3](https://github.com/mattn/go-sqlite3) supports database/sql, based on cgo.
[https://github.com/feyeleanor/gosqlite3](https://github.com/feyeleanor/gosqlite3) doesn't support database/sql, based on cgo.
[https://github.com/phf/go-sqlite3](https://github.com/phf/go-sqlite3)

[Building Web application with Golang](https://astaxie.gitbooks.io/build-web-application-with-golang/en/05.3.html)

[^pass-by-value]: [When are function parameters passed by value? | The Go Programming Language FAQ](https://golang.org/doc/faq#pass_by_value)

[^pass-by-value2]: [There is no pass-by-reference in Go | Dave Cheney](https://dave.cheney.net/2017/04/29/there-is-no-pass-by-reference-in-go)