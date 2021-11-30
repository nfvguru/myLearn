package main

import "log"

func main() {
  var  var1 string
  var1 = "Green"
  log.Println(var1)
  renameme(&var1)
  log.Println(var1)

}

func  renameme(lvar *string){
  newval :=  "Red"
  *lvar = newval
}
