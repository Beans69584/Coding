var fs = require('fs');
var path = require('path');

var dir = 'C:\\Users\\bbean\\Documents\\New coding\\StandaloneTS';
var files = [];

function listdir(dir) {
    var files = fs.readdirSync(dir);
    for (var i in files) {
        var name = dir + '\\' + files[i];
        if (fs.statSync(name).isDirectory()) {
            listdir(name);
        } else {
            console.log(name);
        }
    }
}

listdir(dir);