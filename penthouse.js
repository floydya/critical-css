const penthouse = require('penthouse')
const fetch = require("node-fetch")

let css_url = process.argv[2]
let site_url = process.argv[3]

fetch(css_url)
    .then(resp => resp.text())
    .then(body => {
        penthouse({
            url: site_url,
            cssString: body,
            height: 10000,
            width: 1920
        })
            .then(criticalCss => {
                console.log(criticalCss)
            })
    })
