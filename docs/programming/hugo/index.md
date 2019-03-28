# Hugo Basics

## Templating
### Built-in Functions
#### in[^in_function]
When you need to find out whether a particular value is inside a given string or a slice:

!!! info "Syntax"
    ``` django
    in SET ITEM
    ```

A particular example comes from my current effort to rebuild my blog in Hugo. Certain posts of mine contain the tag _micropost_ and should be rendered differently from the rest. To find those out, I had to do the following:

``` hugo
{{ if in .Params.tags "micropost"}} 
  This is a micropost 
{{ end }}
```

Alternatively, to find the inverse of this, i.e. the posts that are **not** microposts, I had to use the `ne`[^ne_function] function in a combination with `in`. it is a bit more cumbersome, but it works:

``` hugo
{{ if ne true (in .Params.tags "micropost")}}
  This is NOT a micropost
{{ end }}
```

[^in_function]: [in | Hugo Docs](https://gohugo.io/functions/in/)
[^ne_function]: [ne | Hugo Docs](https://gohugo.io/functions/ne/)