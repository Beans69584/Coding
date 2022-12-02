// prints fizz if number divisible by 3, prints buzz if number divisible by 5, prints fizzbuzz if both are true
for (let i = 1; i <= 100000; i++) {
    number = i
    numberfizzthing = number % 3;
    numberbuzzthing = number % 5;
    numberfizzbuzzthing = number % 15;
    numberbazzthing = number % 7;
    if (numberfizzbuzzthing == 0) {
        thingything = "FizzBuzz";
    } else if (numberfizzthing == 0 && numberbuzzthing !== 0 && numberbazzthing !== 0 && numberfizzbuzzthing !== 0) {
        thingything = "Fizz";
    } else if (numberbuzzthing == 0 && numberfizzthing !== 0 && numberbazzthing !== 0 && numberfizzbuzzthing !== 0) {
        thingything = "Buzz";
    } else if (numberbazzthing == 0 && numberfizzbuzzthing !== 0 && numberfizzthing !== 0 && numberbuzzthing !== 0) {
        thingything = "Bazz";
    } else if (numberbazzthing !== 0 && numberfizzbuzzthing !== 0 && numberfizzthing !== 0 && numberbuzzthing !== 0) {
        thingything = number;
    }
    console.log(thingything)
}