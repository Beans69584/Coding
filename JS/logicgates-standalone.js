const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let A = "";
let B = "";
let O = "";

// ask for choice of gate
rl.question(
  "Enter the type of logic gate (AND, OR, XOR, NOT, NAND, NOR, XNOR): ",
  (answer) => {
    O = answer;
    rl.question("Enter the first input: ", (answer) => {
      A = answer;
      rl.question("Enter the second input: ", (answer) => {
        B = answer;
        rl.close();
      });
    });
  }
);

rl.on("close", () => {
  console.clear();
  if (O === "AND") {
    if (A === "1" && B === "1") {
      console.log("Output: 1");
    } else {
      console.log("Output: 0");
    }
  } else if (O === "OR") {
    if (A === "1" || B === "1") {
      console.log("Output: 1");
    } else {
      console.log("Output: 0");
    }
  } else if (O === "XOR") {
    if ((A === "1" && B === "0") || (A === "0" && B === "1")) {
      console.log("Output: 1");
    } else {
      console.log("Output: 0");
    }
  } else if (O === "NOT") {
    if (A === "1") {
      console.log("Output: 0");
    } else {
      console.log("Output: 1");
    }
  } else if (O === "NAND") {
    if (A === "1" && B === "1") {
      console.log("Output: 0");
    } else {
      console.log("Output: 1");
    }
  } else if (O === "NOR") {
    if (A === "1" || B === "1") {
      console.log("Output: 0");
    } else {
      console.log("Output: 1");
    }
  } else if (O === "XNOR") {
    if ((A === "1" && B === "0") || (A === "0" && B === "1")) {
      console.log("Output: 0");
    } else {
      console.log("Output: 1");
    }
  } else {
    console.log("Invalid input");
  }
});
