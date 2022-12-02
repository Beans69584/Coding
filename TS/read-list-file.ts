import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
import * as fs from "node:fs/promises";
const rl2 = readline.createInterface({ input, output });
let a = true;
async function main() {
    const choice = await rl2.question("What would you like to do?\n1.List files\n2.Read file\n3.Quit (Just press ctrl + c)\n");
    if (choice === "1") {
        const files = await fs.readdir("./");
        console.log(files);
    } else if (choice === "2") {
        const path = await rl2.question("What is the path of the file? ");
        const file = await fs.readFile(path, "utf-8");
        console.log(file);
    } else if (choice === "3") {
        a = false;
        rl2.close();
    }
};
(async () => { 
    while (a == true) {
        await main();
    }
})();