package controller

import (
	"greetings-operator/pkg/controller/greetings"
)

func init() {
	// AddToManagerFuncs is a list of functions to create controllers and add them to a manager.
	AddToManagerFuncs = append(AddToManagerFuncs, greetings.Add)
}
