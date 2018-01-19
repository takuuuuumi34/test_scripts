var page = require('webpage').create(),
  system = require('system'),
  t, address;

if (system.args.length === 1) {
  console.log('Usage: loadspeed.js <some URL>');
  phantom.exit();
}

url = system.args[1];
page.onConsoleMessage = function(msg) {
  console.log('Page title is ' + msg);
};

page.open(url, function(status) {
  var title = page.evaluate(function() {
    console.log(document.title);
  });
  
  phantom.exit();
});

