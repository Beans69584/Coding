function countdown() {
  var currentDay = new Date();
  var christmasDay = new Date("2022-12-25 00:00:00");
  var oneDay = 1000 * 60 * 60 * 24;
  var oneHour = 1000 * 60 * 60;
  var oneMinute = 1000 * 60;
  var oneSecond = 1000;
  var daysLeft = Math.floor((christmasDay - currentDay) / oneDay);
  var hoursLeft = Math.floor(((christmasDay - currentDay) % oneDay) / oneHour);
  var minutesLeft = Math.floor(
    (((christmasDay - currentDay) % oneDay) % oneHour) / oneMinute
  );
  var secondsLeft = Math.floor(
    ((((christmasDay - currentDay) % oneDay) % oneHour) % oneMinute) / oneSecond
  );
  var millisecondsLeft = Math.floor(
    ((((christmasDay - currentDay) % oneDay) % oneHour) % oneMinute) % oneSecond
  );
  console.clear();
  document.getElementById("Christmas").innerHTML = "Until Christmas:";
  document.getElementById("timeLeft").innerHTML =
    daysLeft +
    " days, " +
    hoursLeft +
    " hours, " +
    minutesLeft +
    " minutes, " +
    secondsLeft +
    " seconds, " +
    millisecondsLeft +
    " milliseconds";
  console.log(
    "Until Christmas:\n" +
      daysLeft +
      " days, " +
      hoursLeft +
      " hours, " +
      minutesLeft +
      " minutes, " +
      secondsLeft +
      " seconds, " +
      millisecondsLeft +
      " milliseconds"
  );
  if (daysLeft == 0 && hoursLeft == 0 && minutesLeft == 0 && secondsLeft == 0) {
    document.getElementById("Christmas").innerHTML = "Merry Christmas!";
    document.getElementById("timeLeft").innerHTML = "";
    console.log("Merry Christmas!");
  }
}
setInterval(countdown, 0);
