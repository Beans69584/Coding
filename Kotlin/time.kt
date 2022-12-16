fun main() {
    while (true) {
        // clear screen
        print("\u001b[2J\u001b[H")
        val now = java.time.LocalTime.now()
        // format time HH:MM:SS
        val formatter = java.time.format.DateTimeFormatter.ofPattern("HH:mm:ss")
        // print current time
        println("Current time: ${now.format(formatter)}")
        // sleep for 1 second (1000 milliseconds)
        Thread.sleep(1000)
    }
}