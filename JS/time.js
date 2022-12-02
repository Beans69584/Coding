// make a program which will print the current time every second to the console and clear the console before printing the time again.
function time() {
  var date = new Date();
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var seconds = date.getSeconds();
  var time = hours + ":" + minutes + ":" + seconds;
  console.clear();
  console.log(time);
}
setInterval(time, 1000);