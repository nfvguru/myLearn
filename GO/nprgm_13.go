package main
import (
  "log"
  "time"
)


type  firstStruct struct  {
  FirstName string
  LastName string
  Age int
  DateOfBirth time.Time
}


func main() {
  user :=  firstStruct {
    FirstName: "Lavaraj",
    LastName: "Bose",
    Age: 45,
  }
  log.Println(user.FirstName)
}

