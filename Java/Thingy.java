import java.util.Scanner;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

/*
 * Ignore this, it's for my incredibly short term memory
 * Cat myCat = new Cat();
 * myCat.name = "Fred";
 * myCat.age = 6;
 */

public class Thingy {
    public static void writeToFile(String[] args, String filenamething, String myName, float UKshoeSize,
            float USshoeSize) {
        try {
            FileWriter myWriter = new FileWriter(filenamething, true);
            myWriter.write("UK: " + UKshoeSize + " " + "US: " + USshoeSize + " " + myName + "\n");
            myWriter.close();
        } catch (IOException e) {
            System.out.println("An error occured.");
            e.printStackTrace();
        }
    }

    static boolean isInteger(double N) {
        int X = (int) N;
        double temp2 = N - X;
        if (temp2 > 0) {
            return false;
        }
        return true;
    }

    public static void main(String[] args) throws InterruptedException {
        String filenamething = "users.log";
        Scanner myObj = new Scanner(System.in);
        System.out.println("What is your UK shoe size? ");
        int shoeSize;
        float shoeSize2;
        float UKshoeSize = Float.parseFloat(myObj.nextLine());
        float USshoeSize = UKshoeSize + 1;
        double N = USshoeSize;
        if (isInteger(N)) {
            shoeSize = Math.round(USshoeSize);
            System.out.println("Your shoe size in the US is " + shoeSize);
        } else {
            shoeSize2 = USshoeSize;
            System.out.println("Your shoe size in the US is " + shoeSize2);
        }
        Thread.sleep(1000);
        System.out.println("What is your name? ");
        var myName = myObj.nextLine();
        try {
            File myFile = new File("users.log");
            if (myFile.createNewFile()) {
                System.out.println("\n");
                writeToFile(args, filenamething, myName, UKshoeSize, USshoeSize);
            } else {
                writeToFile(args, filenamething, myName, UKshoeSize, USshoeSize);
            }
        } catch (IOException e) {
            System.out.println("An error occured.");
            e.printStackTrace();
        }
        myObj.close();
    }
}
