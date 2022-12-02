import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
import * as fs from "node:fs/promises";

const rl = readline.createInterface({ input, output });
let e = true;
async function calculator() {
  const choice = await rl.question(
    "What would you like to do?\n1.Add\n2.Subtract\n3.Divide\n4.Multiply\n5.Exit\n"
  );

  if (choice === "1") {
    const num1 = await rl.question("What is the first number? ");
    const num2 = await rl.question("What is the second number? ");
    console.log(Number(num1) + Number(num2));
  } else if (choice === "2") {
    const num1 = await rl.question("What is the first number? ");
    const num2 = await rl.question("What is the second number? ");
    console.log(Number(num1) - Number(num2));
  } else if (choice === "3") {
    const num1 = await rl.question("What is the first number? ");
    const num2 = await rl.question("What is the second number? ");
    console.log(Number(num1) / Number(num2));
  } else if (choice === "4") {
    const num1 = await rl.question("What is the first number? ");
    const num2 = await rl.question("What is the second number? ");
    console.log(Number(num1) * Number(num2));
  } else if (choice === "5") {
    e = false;
  } else {
    console.log("Invalid choice");
  }
}
(async () => {
  while (e == true) {
    await calculator();
  }
  rl.close();
})();
