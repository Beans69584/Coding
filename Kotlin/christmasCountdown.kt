fun main() {
    // get the current date and time every time the code is looped 
    while (true) {
        // clear screen 
        print("\u001b[2J\u001b[H")
        var currentDateTime = java.time.LocalDateTime.now() 
        var targetDateTime = java.time.LocalDateTime.of(2022, 12, 25, 0, 0, 0)
        var difference = java.time.Duration.between(currentDateTime, targetDateTime)
        var differenceDays = difference.toDays()
        var differenceHours = difference.toHours() - (differenceDays * 24)
        var differenceMinutes = difference.toMinutes() - (differenceDays * 24 * 60) - (differenceHours * 60)
        var differenceSeconds = difference.seconds - (differenceDays * 24 * 60 * 60) - (differenceHours * 60 * 60) - (differenceMinutes * 60)
        println("Until Christmas 2022:\n$differenceDays days, $differenceHours hours, $differenceMinutes minutes, $differenceSeconds seconds")
        Thread.sleep(1000)
    }
}