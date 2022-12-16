import 'dart:io';

void main() {
    while (true) {
        print("\x1B[2J\x1B[0;0H");
        var currentTime = DateTime.now();
        var currentHour = currentTime.hour;
        var currentMinute = currentTime.minute;
        var currentSecond = currentTime.second;
        print("Current time: $currentHour:$currentMinute:$currentSecond");
        sleep(Duration(seconds: 1));
        // clear the screen
    }
}