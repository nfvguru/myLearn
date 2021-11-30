package main
import "fmt"

type Lava struct {
   FirstName string
   LastName string
   Age int
}

func main() {
   myMap := make(map[string]Lava)
   lavaVar := Lava {
      FirstName:  "Lavaraj",
      LastName: "Bose",
      Age: 45,
   }

   myMap["myself"] = lavaVar

   fmt.Println(myMap["myself"].FirstName)
   fmt.Println(myMap["myself"].LastName)
   fmt.Println(myMap["myself"].Age)

}
