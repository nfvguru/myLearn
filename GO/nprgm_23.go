package mainlava
import (
      "fmt"
      "errors"
    )

func main() {
  fmt.Printf("=======================\n")
  _, err := functionToTest(1)
  if err != nil {
      fmt.Println("Function Failed")
  } else {
      fmt.Println("Function Succeeded")
  }
}


func  functionToTest( val int) (string , error) {
  var  res string 
  res = "completed"

  switch (val) {
  case 1:
    res = "not done"
  case 3:  
    res = "not done"
  case 5:
    res = "not done"
  case 8:
    res = "issue"

  }
  if res !=  "completed" {
    return  res, errors.New("execution error")
  }
  return res, nil


}
