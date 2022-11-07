Concurrency Primitives in GoLang
--------------------------------

* [Practical Example of Concurrency on Golang](https://articles.wesionary.team/practical-example-of-concurrency-on-golang-fc4609ea8ed1) - Go Routine, WaitGroups, Mutex, Channel

`helloworld.go`
```golang
package main

import "fmt"

func main() {
   fmt.Println("Hello World")
}
```

`go run helloworld.go`


---

`/usr/bin/time -f "%e" go run zero.go`

## Zero Concurrency

```golang
package main

import (
	"fmt"
	"net/http"
)

func main() {

	websites := []string{
		"https://stackoverflow.com/",
		"https://github.com/",
		"https://www.linkedin.com/",
		"http://medium.com/",
		"https://golang.org/",
		"https://www.udemy.com/",
		"https://www.coursera.org/",
		"https://wesionary.team/",
	}

	for _, website := range websites {
		getWebsite(website)
	}

}
func getWebsite(website string) {
	if res, err := http.Get(website); err != nil {
		fmt.Println(website, "is down")
	} else {
		fmt.Printf("[%d] %s is up\n", res.StatusCode, website)
	}
}
```

## With WaitGroup
```golang

var wg sync.WaitGroup

func main() {

	websites := []string{
		"https://stackoverflow.com/",
		"https://github.com/",
		"https://www.linkedin.com/",
		"http://medium.com/",
		"https://golang.org/",
		"https://www.udemy.com/",
		"https://www.coursera.org/",
		"https://wesionary.team/",
	}

	for _, website := range websites {
		go getWebsite(website)
		wg.Add(1)
	}

	wg.Wait()

}
func getWebsite(website string) {
	defer wg.Done()
	if res, err := http.Get(website); err != nil {
		fmt.Println(website, "is down")

	} else {
		fmt.Printf("[%d] %s is up\n", res.StatusCode, website)
	}

}
```

## Adding Mutex
```golang

var wg sync.WaitGroup
var mut sync.Mutex

func main() {

	websites := []string{
		"https://stackoverflow.com/",
		"https://github.com/",
		"https://www.linkedin.com/",
		"http://medium.com/",
		"https://golang.org/",
		"https://www.udemy.com/",
		"https://www.coursera.org/",
		"https://wesionary.team/",
	}

	for _, website := range websites {
		go getWebsite(website)
		wg.Add(1)
	}

	wg.Wait()

}
func getWebsite(website string) {
	defer wg.Done()
	if res, err := http.Get(website); err != nil {
		fmt.Println(website, "is down")

	} else {
		mut.Lock()
		defer mut.Unlock()
		fmt.Printf("[%d] %s is up\n", res.StatusCode, website)
	}

}
```

## Goroutines with Channel

```golang

func main() {

	c := make(chan string)

	websites := []string{
		"https://stackoverflow.com/",
		"https://github.com/",
		"https://www.linkedin.com/",
		"http://medium.com/",
		"https://golang.org/",
		"https://www.udemy.com/",
		"https://www.coursera.org/",
		"https://wesionary.team/",
	}

	for _, website := range websites {
		go getWebsite(website, c)
	}

//Iterating over the range of channel. So keeps receiving messages until channel is closed
	for msg := range c {
		fmt.Println(msg)
	}

	//Alternate syntax

	//  for{
	// 	msg,open := <- c
	// 	if(!open){
	// 		break
	// 	}
	// 	fmt.Println(msg)
	// 	}

}
func getWebsite(website string, c chan string) {
	if _, err := http.Get(website); err != nil {
		c <- website + "is down"

	} else {
		c <- website + "is up"
	}

}
```