# Go Project Structure

There are various ways to approach package structure in Go applications, but like other Go topics, the general motto here is, *"don’t do more than you need"*. 

## Very Small Projects

If the application is new, has uncertain requirements, or supposed to stay small for a while (think, a CLI tool or a microservice),  you might be just as fine by putting all of your `.go` files at the root of you project. For reusability, make sure that you keep one file dedicated to hosting your `main` function (e.g. `main.go`). Every other `.go` file should use the name of project as a package (or module name, if you use modules).

```bash
├── main.go —> package main
├── server.go —> package my_project
├── databse.go —> package my_project
├── go.mod
├── go.sum
```

Hint: Keep your main file fairly small. You don’t want a lot of logic in here. Just the basics to get your application going.

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://www.calhoun.io" data-iframely-url="//cdn.iframe.ly/KGN26i1?iframe=card-small"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

## Larger Projects

For bigger projects, use the following structure [^project-structure]:

```bash
├── cmd
│   ├── _your_app_executable_1_
│   │   └── cli.go
│   └── _your_app_executable_2_
│       └── server.go
├── go.mod
├── internal
│   └── logic
│       └── logic.go
└── pkg
    └── http
        └── http.go
```

This structure has been championed by several large projects, and is part of a well-known public [set of guidelines](https://github.com/golang-standards/project-layout) [^project-structure]. Here is what should go into each of these folders:

`/cmd` - is where your `main` file(s) should go. Unlike the simple example above, those can be many (e.g. one CLI, one web server, etc). Separate each of the executables into sub-directories, in order to avoid conflicts. Inside each of the sub-directories, you can include your favourite `main.go` files. You can also name them accordingly. Important is to make sure that they are all inside the `main` package and include a `main` function.

`/internal` - A convention, enforced by the Go compiler since Go 1.4. Any directory with the name `internal` will host packages only accessible for code within the directory as well as for siblings (e.g. the `pkg` and `cmd` directories). This will also any external usage of your “truly private“ Go code, e.g. as part of 3rd-party applications or libraries.

[Use internal packages to reduce your public API surface](https://dave.cheney.net/2019/10/06/use-internal-packages-to-reduce-your-public-api-surface)

`/pkg` - is where you keep code, available for outside use. Unlike `internal` packages within `pkg`can be freely fetched and re-used by 3rd party applications and libraries

[^project-structure]: [golang-standards/project-layout](https://github.com/golang-standards/project-layout)