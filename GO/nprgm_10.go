package main
import (
	"fmt"
	"math/cmplx"
)

var (
	a bool = false
	b uint64 = 1<<64 -1
	c complex128 = cmplx.Sqrt(-5+12i)

)

func main() {
	const f = " Type %T, Value %v\n"
	fmt.Printf(f, a, a)
	fmt.Printf(f, b, b)
	fmt.Printf(f, c, c)
}
