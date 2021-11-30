package main
import "fmt"
func main() {
   var  myBool bool
   var myStr string
   var myInt int

   myBool =  true
   myStr = "lava"
   myInt = 10

   if myBool {
      fmt.Println("myBool is true")
   }

   if myInt > 1 {
      fmt.Println("myInt is greater than 1")
   } else {
      fmt.Println("myInt is greater than 1")
   }

   if myStr == "lava" ||  myInt <  9  {
      fmt.Println("condition 1")
   } else if  !myBool {
      fmt.Println("condition 2")
   } else  {
      fmt.Println("condition 3")
   }


}
