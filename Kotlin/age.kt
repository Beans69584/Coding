// make a program that asks for the users name and age and then tells them whether they are old enough to use the program or not
fun main(args: Array<String>) {
    println("Hello, World!")
    println("What is your name?")
    val name = readLine()
    println("What is your age?")
    val age = readLine()
    if (age!!.toInt() < 18) {
        println("You are not old enough to use this program")
    } else {
        println("Welcome to the program $name")
    }
}