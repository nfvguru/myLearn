package main
import "fmt"

type  mystruct struct {
  FirstName string
}

func (vv *mystruct) printFiN() string {
  return  vv.FirstName
}

func main() {
  var  var1 mystruct
  var1.FirstName = "lavanz"
  var2 := mystruct {
    FirstName: "lalu",
  }
  fmt.Println(var1.printFiN(), var2.printFiN())

}
