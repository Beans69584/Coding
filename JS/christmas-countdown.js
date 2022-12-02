
function countdown() {
    var currentYear = new Date().getFullYear();
    var currentDay = new Date();
    var christmasDay = new Date(`December 25, ${currentYear}`);
    var oneDay = 1000 * 60 * 60 * 24;
    var oneHour = 1000 * 60 * 60;
    var oneMinute = 1000 * 60;
    var oneSecond = 1000;
    var daysLeft = Math.floor((christmasDay - currentDay) / oneDay);
    var hoursLeft = Math.floor(((christmasDay - currentDay) % oneDay) / oneHour);
    var minutesLeft = Math.floor((((christmasDay - currentDay) % oneDay) % oneHour) / oneMinute);
    var secondsLeft = Math.floor(((((christmasDay - currentDay) % oneDay) % oneHour) % oneMinute) / oneSecond);
    console.clear();
    console.log("Until Christmas " + currentYear + ":" + "\n" + daysLeft + " days, " + hoursLeft + " hours, " + minutesLeft + " minutes, " + secondsLeft + " seconds");
  }
    setInterval(countdown, 1000);