package main
import "fmt"
func main() {
   myStr:= "fish"

   switch myStr {
     case "dog" :
        fmt.Println("This is happy")
     case "fish" :
        fmt.Println("This is happy")
        fmt.Println("I got fish")
     default :
        fmt.Println("This is NoT happy")

   }
}
