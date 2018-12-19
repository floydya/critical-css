const penthouse = require('penthouse');
const fetch = require("node-fetch");

let css_url = process.argv[2];
let site_url = process.argv[3];
let width = process.argv[4];
let height = process.argv[5];

fetch(css_url)
    .then(resp => resp.text())
    .then(body => {
        penthouse({
            url: site_url,
            cssString: body,
            width: width,
            height: height
        })
            .then(criticalCss => {
                console.log(criticalCss)
            })
    });
