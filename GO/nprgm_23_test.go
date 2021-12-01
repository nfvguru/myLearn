package mainlava
import "testing"

var tests = [] struct {
   name string
   input int
   expected string
   goterr bool
} {
  {"test1", 1, "not done", true},
  {"test1", 2, "completed", false},
  {"test1", 3, "not done", true},
  {"test1", 4, "completed", false},
}


func TestFunctionToTest( t *testing.T) {
  for _,tt := range tests {
     res, err := functionToTest(tt.input)
     if tt.goterr {
        if err == nil {
	   t.Error("function supposed return error. but missing err")
	}
     } else {
        if err != nil {
	   t.Error("Function should work without error. but got err", err.Error())
	}
     }
	
     if res != tt.expected {
        t.Errorf("expected %s , got %s", tt.expected, res)
     }


  }
}
