package main
import ( 
  "fmt" 
  "math/rand"
  "time"
)

func  myCalc(intLav chan int) {
    rand.Seed(time.Now().UnixNano())
    value := rand.Intn(1000)
    intLav <- value
    
}


func main() {
  intLalu :=make(chan int)
  defer  close(intLalu)

  go myCalc(intLalu)
  num := <-intLalu
  fmt.Println(num)
}
