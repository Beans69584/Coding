function secondsLived(age) {
  return age * 365 * 24 * 60 * 60;
}
function Main() {
  var age = 14;
  var seconds = secondsLived(age);
  console.log(seconds);
}
Main();