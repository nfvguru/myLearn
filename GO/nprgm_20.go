package main
import "fmt"

type Lava interface {
   NoTyres() int
   Usage() string
}

type  Car struct {
   brand string
   model string
}

type  Scooter struct {
   model string
   age  int
}

func ( c *Car) NoTyres() int {
  return 4
}

func ( s *Scooter) NoTyres() int {
  return 2
}


func main() {

   mycars :=  Car {
     brand: "Ford",
   }
   printD(&mycars)
   mySco := Scooter {
      age: 4,
   }
   printD(&mySco)
}

func printD (l Lava) {
  fmt.Println(l)
  fmt.Println("Vehicle has ", l.NoTyres(), "tyres and ", l.Usage(), "usage")
}

func ( c *Car) Usage() string {
  return "weekly"
}

func ( s *Scooter) Usage() string {
  return "daily"
}


