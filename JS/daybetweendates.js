function daysUntil(date1, date2) {
    var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
    var firstDate = new Date(date1);
    var secondDate = new Date(date2);
    var diffDays = Math.round(Math.abs((firstDate.getTime() - secondDate.getTime())/(oneDay)));
    diffDays = diffDays - 1;
    return diffDays;
}
function Main() {
    var date1 = new Date(2022, 11, 24);
    var date2 = new Date(2022, 12, 25);
    var days = daysUntil(date1, date2);
    console.log(days);
}
Main();