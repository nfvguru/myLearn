package main
import "log"
var  s = "seven"

func main() {
  var s2 = "six"
  log.Println(s)
  log.Println(s2)
  s2, s3 := myfunc2("lava is")
  log.Println(s2, s3)
}


func  myfunc2 (s string) (string, string) {
  return s, "cool"
}
