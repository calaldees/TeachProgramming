Concurrency Primitives in GoLang
--------------------------------

* see [[async-await]]
* Concurrency
	* [Asyncio, twisted, tornado, gevent walk into a bar ... they pay, they leave, they drink, they order.](https://www.bitecode.dev/p/asyncio-twisted-tornado-gevent-walk)
		* URL fetch example with 3 different python async systems
		* The typical analogy is this:
			* concurrency is having two lines of customers ordering from a one cashier;
			* parallelism is having two lines of customers ordering from two cashiers.
		* Which, means, if you think about it, that concurrency has a lot to do with sharing one resource
		* `async` just isn't needed - Python Documentation [ThreadPoolExecutor Example](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example) multiple urls
		* Discuss's FastAPI and Django
	* [Notes on structured concurrency, or: Go statement considered harmful](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/)
* Concurrency and Parallelisation are different concepts
	* Concurrency - quickly switching between multiple tasks to keep all the plates spinning
		* one person laying bricks and mortar and taking a few phone calls throughout a day
	* Parallelisation - doing multiple tasks at the same time
		* 12 people laying bricks and mortaring at the same time with an overseer making phone calls


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
package main

import (
	"fmt"
	"net/http"
	"sync"
)

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
package main

import (
	"fmt"
	"net/http"
	"sync"
)

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
package main

import (
	"fmt"
	"net/http"
	"sync"
)


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