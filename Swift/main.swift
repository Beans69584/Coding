import Foundation 
print("Hello, World!")
// ask the user for their name and age 
print("What is your name?")
let name = readLine()!
print("What is your age?")
let age = readLine()!
if let age = Int(age), age >= 13 {
    print("Hello \(name), you are \(age) years old.")
} else {
    print("Hello \(name), you are not old enough to use this program.")
}

// wait for the user to press a key before exiting
print("Press any key to exit...")
_ = readLine()