package main

import (
	"fmt"
	"time"
)

func main() {
	dateFormat := "01/02/2006"
	today := time.Now()
	todayString := today.Format(dateFormat)

	var yourBirthday string
	fmt.Print("Your birthday (Example: 07/11/1997): ")
	fmt.Scanln(&yourBirthday)

	a, err := time.Parse(dateFormat, yourBirthday)
	if err != nil {
		fmt.Println(err)
		return
	}
	b, err := time.Parse(dateFormat, todayString)
	if err != nil {
		fmt.Println(err)
		return
	}
	delta := b.Sub(a)
	fmt.Printf("As of today you are %d days old.", int(delta.Hours()/24))
}
