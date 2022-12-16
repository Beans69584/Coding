import 'dart:io';
void main() {
    print("\x1B[2J\x1B[0;0H");
    var programName = "Dart";
    print("Enter your age: ");
    var age = stdin.readLineSync();
    if (age == "0" || age == "1" || age == "2" || age == "3" || age == "4" || age == "5" || age == "6" || age == "7" || age == "8" || age == "9" || age == "10" || age == "11" || age == "12") {
        print("You are too young to use this program.");
        exit(0);
    }
    print("Enter your name: ");
    var name = stdin.readLineSync();
    print("Hello $name, welcome to $programName");
    logicGates();
}
logicGates() {
    sleep(Duration(milliseconds: 500));
    print("Welcome! This program will help you to understand the logic gates.");
    sleep(Duration(milliseconds: 500));
    print("Which logic gate would you like to simulate?");
    sleep(Duration(milliseconds: 500));
    print("1. AND\n2. OR\n3. NOT\n4. NAND\n5. NOR\n6. XOR\n7. XNOR");
    var gate = stdin.readLineSync();
    switch (gate) {
        case "1":
            print("Enter the first input: ");
            var input1 = stdin.readLineSync();
            print("Enter the second input: ");
            var input2 = stdin.readLineSync();
            if (input1 == "1" && input2 == "1") {
                print("Output: 1");
            } else {
                print("Output: 0");
            }
            break;
        case "2":
            print("Enter the first input: ");
            var input1 = stdin.readLineSync();
            print("Enter the second input: ");
            var input2 = stdin.readLineSync();
            if (input1 == "1" || input2 == "1") {
                print("Output: 1");
            } else {
                print("Output: 0");
            }
            break;
        case "3":
            print("Enter the input: ");
            var input = stdin.readLineSync();
            if (input == "1") {
                print("Output: 0");
            } else {
                print("Output: 1");
            }
            break;
        case "4":
            print("Enter the first input: ");
            var input1 = stdin.readLineSync();
            print("Enter the second input: ");
            var input2 = stdin.readLineSync();
            if (input1 == "1" && input2 == "1") {
                print("Output: 0");
            } else {
                print("Output: 1");
            }
            break;
        case "5":
            print("Enter the first input: ");
            var input1 = stdin.readLineSync();
            print("Enter the second input: ");
            var input2 = stdin.readLineSync();
            if (input1 == "1" || input2 == "1") {
                print("Output: 0");
            } else {
                print("Output: 1");
            }
            break;
        case "6":
            print("Enter the first input: ");
            var input1 = stdin.readLineSync();
            print("Enter the second input: ");
            var input2 = stdin.readLineSync();
            if (input1 == "1" && input2 == "0" || input1 == "0" && input2 == "1") {
                print("Output: 1");
            } else {
                print("Output: 0");
            }
            break;
        case "7":
            print("Enter the first input: ");
            var input1 = stdin.readLineSync();
            print("Enter the second input: ");
            var input2 = stdin.readLineSync();
            if (input1 == "1" && input2 == "1" || input1 == "0" && input2 == "0") {
                print("Output: 1");
            } else {
                print("Output: 0");
            }
            break;
        default:
            print("Invalid input!");
}
// clear the screen
sleep(Duration(seconds: 2));
// clear the screen 
print("\x1B[2J\x1B[0;0H");
logicGates();
}