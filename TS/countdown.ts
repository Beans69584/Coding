import { setInterval } from "timers";
console.info("Only works for World Cup 2022");
setTimeout(() => {
  console.clear();
}, 1000);
setInterval(() => {
  var currentDate = new Date();
  var targetDate = new Date("2022-12-10 19:00:00");
  var difference = targetDate.getTime() - currentDate.getTime();
  var days = Math.floor(difference / (1000 * 60 * 60 * 24));
  var hours = Math.floor(
    (difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  var minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((difference % (1000 * 60)) / 1000);
  var milliseconds = Math.floor(difference % 1000);
  console.clear();
  console.log(
    "Until England vs France: \n" +
      days +
      " days " +
      hours +
      " hours " +
      minutes +
      " minutes " +
      seconds +
      " seconds " +
      milliseconds +
      " milliseconds"
  );
}, 0);
