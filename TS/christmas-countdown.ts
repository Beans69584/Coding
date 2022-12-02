import { setInterval } from "timers";
console.info("Only works for christmas 2022");
setTimeout(() => {
  console.clear();
}, 1000);
setInterval(() => {
  var currentYear = new Date().getFullYear();
  var currentDate = new Date();
  var targetDate = new Date(`{currentYear}-12-25 00:00:00`);
  var difference = targetDate.getTime() - currentDate.getTime();
  var days = Math.floor(difference / (1000*60*60*24));
  var hours = Math.floor((difference % (1000*60*60*24)) / (1000*60*60));
  var minutes = Math.floor((difference % (1000*60*60)) / (1000*60));
  var seconds = Math.floor((difference % (1000*60)) / 1000);
  console.clear();
  console.log("Until Christmas 2022: \n" + days + " days " + hours + " hours " + minutes + " minutes " + seconds + " seconds ");
}, 500);