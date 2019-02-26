const penthouse = require('penthouse');
const fetch = require("node-fetch");

let css_url = process.argv[2];
let site_url = process.argv[3];
let width = process.argv[4];
let height = process.argv[5];

fetch(css_url)
    .then(resp => {
        if (resp.status != 200) {
            throw new Error("Not 200 response!");
        }
        return resp.text();
    })
    .then(body => {
        penthouse({
            url: site_url,
            cssString: body,
            width: width,
            height: height,
            customPageHeaders: {"Penthouse": "critical-css"}
        }).then(criticalCss => {
            console.log(criticalCss)
        })
    });
