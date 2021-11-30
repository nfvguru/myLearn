package main
import "fmt"


func main() {
  type Lava struct {
    FirstName string
    LastName string
    Age int
  }
  mySlice :=  []string{"one","two","three"}
  var myMap = make(map[string]string)
  myMap["one"] = "lavanz"
  myMap["two"] = "kuttan"
  myMap["three"] = "pappus"

  /* myStr := Lava {
    FirstName: "lava",
    LastName: "raj",
    Age:33,
  }*/
  var myStr []Lava
  myStr = append ( myStr, Lava{"Lavaraj","Bose", 45})
  myStr = append ( myStr, Lava{"Seetha","K", 42})
  myStr = append ( myStr, Lava{"Gayathri","Lavaraj", 10})
  myStr = append ( myStr, Lava{"Gauri","Lavaraj", 9})

  fmt.Println("================= simple for loop for 10 =====")
  for i := 0; i < 10; i++ {
    fmt.Println(i)
  }

  fmt.Println("================= range of a slice =====")
  for i,str  := range mySlice {
    fmt.Println(i , "is", str)
  }

  fmt.Println("================= range of a slice without index =====")
  for _,str  := range mySlice  {
    fmt.Println("value is", str)
  }

  fmt.Println("================= range of a map =====")
  for  ky,str := range myMap  {
    fmt.Println(ky , "is", str)
  }

  fmt.Println("================= range of a slice of structs =====")
  for  ky,str := range myStr  {
    fmt.Println(ky , "is", str)
  }
}
