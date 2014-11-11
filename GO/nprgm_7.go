package main
import "fmt"
func myfu( x int) ( a,b int) {
	a = x / 2
	b = x / 3
	return
}
func main() {
	fmt.Println(myfu(12))
}
