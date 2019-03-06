# Go: Web Development
## The Simplest Web Server

!!! note
    The signature of `func(w http.ResponseWriter, r *http.Request)` is a common way of handling HTTP requests throughout the Go standard library. It perfectly complies with the expected `ServeHTTP` method signature of Go's `Handler` interface:[^handler]

    ```go
    type Handler interface {
	    ServeHTTP(ResponseWriter, *Request)
    }
    ```

```go
package main

import (
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte(`
			<html>
				<head>
				<title>Hello World</title>
				</head>
				<body>
					Hello World!
				</body>
			</html>
    	`))
	})

	if err := http.ListenAndServe(":8000", nil); err != nil {
		log.Fatal("ListenAndServe", err)
	}
}
```

[^handler]: [Go’s http package by example](https://cryptic.io/go-http/)

## Frequently Asked Questions
### How do I create a Handler without having to implement an interface?
Sometimes, you would need to provide an instance that conforms to the  `Handler` interface, but want to avoid actually implementing the interface. In this case, you might use the `http.HandlerFunc` (please, note the difference between `http.HandleFunc` and `http.HandlerFunc`):[^handlerfunc]

!!! info "http.HandlerFunc"

	```go
	// The HandlerFunc type is an adapter to allow the use of
	// ordinary functions as HTTP handlers. If f is a function
	// with the appropriate signature, HandlerFunc(f) is a
	// Handler that calls f.
	type HandlerFunc func(ResponseWriter, *Request)

	// ServeHTTP calls f(w, r).
	func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request) {
		f(w, r)
	}
	```

Looking at it carefully, will help you grasp a crucial part of Go's magic - the fact that everything, including functions, is a type, which you can attach further functions upon. In this case, `ServeHTTP` is actually implemented for us inside `http` and essentially proxies to the function we pass as parameter to `HandlerFunc`.

[^handlerfunc]: [type HandlerFunc | Go Docs](https://golang.org/src/net/http/server.go?s=59707:59754#L1987)
