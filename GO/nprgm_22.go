package main
import (
          "encoding/json"
          "fmt"
	)


type Lava struct {
  Name string `json:"name"`
  Age  string `json:"age"`
}


func main() {

  myJson := `
  [
   {
      "name": "lava",
      "age": "10"
   },
   {
     "name": "binu",
     "age": "11"

   }

  ]`

  var lavamarshelled []Lava
  err := json.Unmarshal([]byte(myJson), &lavamarshelled)
  if  err != nil {
    fmt.Println(err)
  }
  fmt.Println("====================== Json to slice of struct =========")
  fmt.Printf("value %v\n", lavamarshelled)
  
  fmt.Println("====================== slice of struct to json =========")

  var mySlice []Lava
  var  m1 Lava
  m1.Name = "lalu"
  m1.Age =  "12"
  mySlice = append(mySlice, m1)
  var  m2 Lava
  m2.Name = "aadi"
  m2.Age =  "13"
  mySlice = append(mySlice, m2)

  fmt.Println(mySlice)
  fmt.Println("after converting")
  newJson, err :=  json.MarshalIndent(mySlice, "", "   ")
  if err != nil {
     fmt.Println(err)
  }
  fmt.Println(string(newJson))





}
