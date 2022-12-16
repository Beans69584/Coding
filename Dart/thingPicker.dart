import 'dart:math';
import 'dart:convert';
import 'dart:io';
void main() {
    var count = 7;
    var finalList = [];
    var watchList = [
    'Deck the Halls',
    'Home Alone',
    'Love is War',
    'Spirited (with Ryan Reynolds)',
    'The Grinch',
    'Bunny Girl Senpai',
    'Nativity!'
    ];
    while (count > 0) { 
        var random = Random();
        var index = random.nextInt(watchList.length);
        var movie = watchList[index];
        finalList.add(movie);
        watchList.removeAt(index);
        count--;
    }
    // sort finalList randomly without using nextDouble()
    finalList.sort((a, b) => Random().nextInt(3) - 1);
    var myJson = jsonEncode(finalList);
    File('movies.json').writeAsString(myJson);
}