import { setInterval } from "timers";

setInterval(() => {
  console.clear();
  console.log(new Date().toLocaleTimeString());
}, 1000);