const fs = require('fs');

const file = 'index.html';
let html = fs.readFileSync(file, 'utf8');

// #1DE9B6 (Teal) is currently Content Marketing.
// #B388FF (Violet) is currently Google Business Profile.
// We swap them.

let newHtml = html.replace(/#1DE9B6/gi, '#TEMP_COLOR');
newHtml = newHtml.replace(/#B388FF/gi, '#1DE9B6');
newHtml = newHtml.replace(/#TEMP_COLOR/gi, '#B388FF');

fs.writeFileSync(file, newHtml, 'utf8');
console.log("Successfully swapped colors between Content Marketing and Google Business Profile.");
