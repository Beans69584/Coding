
fun main() {
    var loopingThingy = true;
    while (loopingThingy == true) {
        println("Welcome!");
        println("1.AND\n2.OR\n3.NOT\n4.XOR\n5.NAND\n6.NOR\n7.XNOR\n8.EXIT\n");
        println("Choose a logic gate:");
        val gate = readLine();
        if (gate == "8") {
            Thread.sleep(1000);
            loopingThingy = false;
        } else if (gate == "1" || gate == "2" || gate == "3" || gate == "4" || gate == "5" || gate == "6" || gate == "7") {
            println("Enter the first input (0/1):");
            val input1 = readLine();
            println("Enter the second input (0/1):");
            val input2 = readLine();
            if (gate == "1") {
                if (input1 == "1" && input2 == "1") {
                    println("Output: 1");
                } else if (input1 == "0" || input2 == "0") {
                    println("Output: 0");
                } else {
                    println("Invalid input");
                }
                Thread.sleep(1000);
            } else if (gate == "2") {
                if (input1 == "1" || input2 == "1") {
                    println("Output: 1");
                } else if (input1 == "0" && input2 == "0") {
                    println("Output: 0");
                } else {
                    println("Invalid input");
                }
                Thread.sleep(1000);
            } else if (gate == "3") {
                if (input1 == "0" && input2 == "0") {
                    println("Output: 1");
                } else if (input1 == "1" || input2 == "1") {
                    println("Output: 0");
                } else {
                    println("Invalid input");
                }
                Thread.sleep(1000);
            } else if (gate == "4") {
                if (input1 == "1" && input2 == "0") {
                    println("Output: 1");
                } else if (input1 == "0" && input2 == "1") {
                    println("Output: 1");
                } else if (input1 == input2) {
                    println("Output: 0");
                } else {
                    println("Invalid input");
                }
                Thread.sleep(1000);
            } else if (gate == "5") {
                if (input1 == "1" && input2 == "1") {
                    println("Output: 0");
                } else if (input1 == "0" || input2 == "0") {
                    println("Output: 1");
                } else {
                    println("Invalid input");
                }
                Thread.sleep(1000);
            } else if (gate == "6") {
                if (input1 == "0" && input2 == "0") {
                    println("Output: 1");
                } else if (input1 == "1" || input2 == "1") {
                    println("Output: 0");
                } else {
                    println("Invalid input");
                }
                Thread.sleep(1000);
            } else if (gate == "7") {
                if (input1 == "1" && input2 == "1") {
                    println("Output: 1");
                } else if (input1 == "0" && input2 == "0") {
                    println("Output: 1")
                } else if (input1 == "0" && input2 == "1") {
                    println("Output: 0");
                } else if (input1 == "1" && input2 == "0") {
                    println("Output: 0")
                } else {
                    println("Invalid input");
                }
                Thread.sleep(1000);
            } else {
                println("Invalid input");
            }
    }
}}