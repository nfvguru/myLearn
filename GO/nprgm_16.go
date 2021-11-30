package main
import "fmt"


func main() {
   var mySlice1 []string
   mySlice1 = append(mySlice1, "one")
   mySlice1 = append(mySlice1, "two")
   mySlice1 = append(mySlice1, "three")
   fmt.Println(mySlice1)

   mySlice2 := []int{1,2,3,4,5,6}
   fmt.Println(mySlice2)
   fmt.Println(mySlice2[5])
   fmt.Println(mySlice2[3:5])
    
}
