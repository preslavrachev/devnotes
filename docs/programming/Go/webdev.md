# Go: Web Development
### The Simplest Web Server

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