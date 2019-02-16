# SQLite ORM Example

inspired by [GORM Quick Start](http://gorm.io/docs/index.html#Quick-Start)

``` go
package main

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

type Person struct {
	gorm.Model
	Name string `json:"name"`
}

func main() {
    db, err := gorm.Open("sqlite3", "./db.sqlite")
    defer db.Close()
    db.AutoMigrate(&Person{})

    me := Person{
		Name: "Preslav",
	}

    db.NewRecord(me)
	db.Create(&me)
}
```